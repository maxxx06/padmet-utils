# -*- coding: utf-8 -*-
"""
Description:
    From a file containing a list of reaction, return the pathways where theses reactions 
    are involved.
    ex: if rxn-a in pwy-x => return, pwy-x; all rxn ids in pwy-x; all rxn ids in pwy-x FROM the list; ratio

::
    
    usage:
        get_pwy_from_rxn.py --reaction_file=FILE --padmetRef=FILE  --output=FILE
    
    options:
        -h --help     Show help.
        --reaction_file=FILE    pathname of the file containing the reactions id, 1/line 
        --padmetRef=FILE    pathname of the padmet representing the database.
        --output=FILE    pathname of the file with line = pathway id, all reactions id, reactions ids from reaction file, ratio. sep = "\t"
"""
from padmet.classes import PadmetSpec
import docopt

def main():
    args = docopt.docopt(__doc__)
    reaction_file = args["--reaction_file"]
    with open(reaction_file, 'r') as f:
        reactions = set(f.read().splitlines())
    padmet_file = args["--padmetRef"]
    output = args["--output"]
    padmet = PadmetSpec(padmet_file)
    dict_pwy = extract_pwys(padmet, reactions)
    dict_pwys_to_file(dict_pwy, output)

def extract_pwys(padmet, reactions):
    """
    #extract from

    Parameters
    ----------
    padmet: padmet.classes.PadmetSpec
        padmet to udpate
    reactions: set
        set of reactions to match with pathways
        
    Returns
    -------
    dict:
        dict, k=pathway_id, v=dict: k in [total_rxn, rxn_from_list, ratio
        ex: {pwy-x:{'total_rxn':[a,b,c], rxn_from_list:[a], ratio:1/3}}
    """
    dict_pwy = {}
    pwys_id = [node.id for node in padmet.dicOfNode.values() if node.type == "pathway"]
    for pwy_id in pwys_id:
        rxn_in_pwy = set([rlt.id_in for rlt in padmet.dicOfRelationOut[pwy_id] if rlt.type == "is_in_pathway" and padmet.dicOfNode[rlt.id_in].type == "reaction"])
        rxn_from_list = reactions.intersection(rxn_in_pwy)
        if rxn_from_list:
            ratio = round(float(len(rxn_from_list))/float(len(rxn_in_pwy)),2)
            dict_pwy[pwy_id] = {'total_rxn': rxn_in_pwy, 'rxn_from_list': rxn_from_list, 'ratio': ratio}
    return dict_pwy
    
def dict_pwys_to_file(dict_pwy, output):
    """
    Create csv file from dict_pwy. dict_pwy is obtained with extract_pwys()

    Parameters
    ----------
    dict_pwy: dict
        dict, k=pathway_id, v=dict: k in [total_rxn, rxn_from_list, ratio
        ex: {pwy-x:{'total_rxn':[a,b,c], rxn_from_list:[a], ratio:1/3}}
    output: str
        path to output file

    """
    with open(output, 'w') as f:
        header = ["pathway_id","total_rxn","rxn_from_list","ratio"]
        f.write("\t".join(header)+"\n")
        for pwy_id, pwy_data in dict_pwy.items():
            total_rxn = pwy_data['total_rxn']
            rxn_from_list = pwy_data['rxn_from_list']
            ratio = pwy_data['ratio']

            line = [pwy_id, ";".join(total_rxn), ";".join(rxn_from_list),str(ratio)]
            f.write("\t".join(line)+"\n")

    
if __name__ == "__main__":
    main()    