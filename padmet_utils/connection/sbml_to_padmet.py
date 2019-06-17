# -*- coding: utf-8 -*-
"""
Description:
    There are 3 cases of convertion sbml to padmet:
    
    1./ Creation of a reference database in padmet format from sbml(s) (or updating one with new(s) sbml(s))
    First usage, padmetRef is the padmetRef to create or to update. If it's an update case, the output
    can be used to create a new padmet, if output None, will overwritte the input padmetRef.
    
    2./ Creation of a padmet representing an organism in padmet format from sbml(s) (or updating one with new(s) sbml(s))
    2.A/ Without a database of reference:
    Second usage, padmetSpec is the padmetSpec to create or update. If it's an update case, the output
    can be used to create a new padmet, if output None, will overwritte the input padmetSpec.
    
    2.B/ With a database of refence:
    Third usage, padmetSpec is the padmetSpec to create or update. If it's an update case, the output
    can be used to create a new padmet, if output None, will overwritte the input padmetSpec.
    padmetRef is the padmet representing the database of reference.
    
    It is possible to define a specific policy and info for the padmet. To learn more about
    policy and info check doc of lib.padmetRef/Spec.
    if the ids of reactions/compounds are not the same between padmetRef and the sbml, it is possible to use
    a dictionnary of association (sbml_id padmetRef_id)
    with one line = 'id_sbml \t id_padmetRef'
    Finally if a reaction from sbml is not in padmetRef, it is possible to force the copy and creating
    a new reaction in padmetSpec with the arg -f

::
    
    usage:
        sbml_to_padmet.py --sbml=FILE --padmetRef=FILE [--output=FILE] [--db=STR] [--version=STR] [-v]
        sbml_to_padmet.py --sbml=FILE --padmetSpec=FILE [--output=FILE] [--db=STR] [--version=STR] [-v]
        sbml_to_padmet.py --sbml=FILE --padmetSpec=FILE [--padmetRef=FILE] [--output=FILE] [--mapping=FILE] [--source_tool=STR] [--source_category=STR] [--source_id=STR] [-v] [-f]
    
    options:
        -h --help     Show help.
        --padmetSpec=FILE    path to the padmet file to update with the sbml. If there's no padmetSpec, just specify the output
        --padmetRef=FILE    path to the padmet file representing to the database of reference (ex: metacyc_18.5.padmet)
        --sbml=FILE    1 sbml file to convert into padmetSpec (ex: my_network.xml/sbml) OR a directory with n SBML
        --output=FILE   pathanme to the new padmet file
        --mapping=FILE    dictionnary of association id_origin id_ref
        --db=STR    database name
        --version=STR    database version
        -v   print info
"""
from padmet.classes import PadmetSpec, PadmetRef
from time import time
from datetime import datetime
import os
import docopt

def main():
    args = docopt.docopt(__doc__)
    padmetRef_file = args["--padmetRef"]
    sbml = args["--sbml"]
    output = args["--output"]
    verbose = args["-v"]
    db = args["--db"]
    if not db: db = "NA"
    version = args["--version"]
    if not version: version = "NA"
    padmetSpec_file = args["--padmetSpec"]
    source_tool = args["--source_tool"]
    source_category = args["--source_category"]
    source_id = args["--source_id"]
    mapping = args["--mapping"]

    padmet = from_sbml_to_padmet(sbml, padmetSpec_file, source_tool, source_category, source_id, padmetRef_file, mapping, db, version, verbose)
    if output:
        padmet.generateFile(output)
    else:
        padmet.generateFile(padmetSpec_file)
        
    
def from_sbml_to_padmet(sbml, padmetSpec_file, source_tool, source_category, source_id, padmetRef_file, mapping, db="NA", version="NA", verbose=False):
    """
    """
    if os.path.isdir(sbml):
        sbml_type = "dir"
    elif os.path.isfile(sbml):
        sbml_type = "file"
    else:
        raise TypeError("%s is not a dir or a file" %(sbml))

    if padmetRef_file:
        if os.path.isfile(padmetRef_file):
            padmetRef = PadmetRef(padmetRef_file)
        else:
            raise IOError("No such file %s" %padmetRef_file)
    else:
        padmetRef = None

    if padmetSpec_file:
        if os.path.isfile(padmetSpec_file):
            padmetSpec = PadmetSpec(padmetSpec_file)
    else:
        now = datetime.now()
        today_date = now.strftime("%Y-%m-%d")

        padmetSpec = PadmetSpec()
        if padmetRef:
            padmetSpec.setInfo(padmetRef)
            padmetSpec.info["PADMET"]["creation"] = today_date
            padmetSpec.setPolicy(padmetRef)
        else:
            POLICY_IN_ARRAY = [['class','is_a_class','class'], ['class','has_name','name'], ['class','has_xref','xref'], ['class','has_suppData','suppData'],
                            ['compound','is_a_class','class'], ['compound','has_name','name'], ['compound','has_xref','xref'], ['compound','has_suppData','suppData'],
                            ['gene','is_a_class','class'], ['gene','has_name','name'], ['gene','has_xref','xref'], ['gene','has_suppData','suppData'], ['gene','codes_for','protein'],
                            ['pathway','is_a_class','class'], ['pathway','has_name','name'], ['pathway','has_xref','xref'], ['pathway','is_in_pathway','pathway'],
                            ['protein','is_a_class','class'], ['protein','has_name','name'], ['protein','has_xref','xref'], ['protein','has_suppData','suppData'], ['protein','catalyses','reaction'],
                            ['protein','is_in_species','class'],
                            ['reaction','is_a_class','class'], ['reaction','has_name','name'], ['reaction','has_xref','xref'], ['reaction','has_suppData','suppData'], ['reaction','has_reconstructionData','reconstructionData'], ['reaction','is_in_pathway','pathway'],
                            ['reaction','consumes','class','STOICHIOMETRY','X','COMPARTMENT','Y'], ['reaction','produces','class','STOICHIOMETRY','X','COMPARTMENT','Y'],
                            ['reaction','consumes','compound','STOICHIOMETRY','X','COMPARTMENT','Y'], ['reaction','produces','compound','STOICHIOMETRY','X','COMPARTMENT','Y'],
                            ['reaction','consumes','protein','STOICHIOMETRY','X','COMPARTMENT','Y'], ['reaction','produces','protein','STOICHIOMETRY','X','COMPARTMENT','Y'],
                            ['reaction','is_linked_to','gene','SOURCE:ASSIGNMENT','X:Y']]
            dbNotes = {"PADMET":{"creation":today_date,"version":"2.6"},"DB_info":{"DB":db,"version":version}}
            padmetSpec.setInfo(dbNotes)
            padmetSpec.setPolicy(POLICY_IN_ARRAY)

    #if sbml is a directory, recover all file path in a list. if no => only one file: create a list with only this file
    sbml_mapping_dict = {}
    if sbml_type == "dir":
        path = sbml
        if not path.endswith("/"):
            path += "/"
        all_files = [i for i in next(os.walk(path))[2] if not i.startswith(".~lock")]
        for sbml_file in [i for i in all_files if i.endswith(".sbml") or i.endswith(".xml")]:
            mapping_file = os.path.splitext(sbml_file)[0] + "_dict.csv"
            if mapping_file not in all_files:
                mapping_file = None
            else:
                mapping_file = path+mapping_file
            sbml_file = path+sbml_file
            sbml_mapping_dict[sbml_file] = mapping_file
    else:
        sbml_mapping_dict[sbml] = mapping

    for sbml_file, mapping_file in list(sbml_mapping_dict.items()):
        if mapping_file:
            force = False
        else:
            force = True

        if padmetSpec_file:
            if verbose:
                if mapping_file:
                    print("Updating %s from %s using mapping dictionnary %s" %(os.path.basename(padmetSpec_file),os.path.basename(sbml_file),os.path.basename(mapping_file)))
                else:
                    print("Updating %s from %s" %(os.path.basename(padmetSpec_file),os.path.basename(sbml_file)))
        else:
            if verbose:
                if mapping_file:
                    print("Updating padmet from %s using mapping dictionnary %s" %os.path.basename(sbml_file),os.path.basename(mapping_file))
                else:
                    print("Updating padmet from %s" %os.path.basename(sbml_file))
        padmetSpec.updateFromSbml(sbml_file, padmetRef = padmetRef, verbose = verbose, source_category = source_category, source_id = source_id, source_tool = source_tool, mapping_file = mapping_file, force = force )

    if len(list(sbml_mapping_dict.keys())) == 0:
        if verbose: print("No sbml found in %s" %sbml)

    return padmetSpec


if __name__ == "__main__":
    main()
