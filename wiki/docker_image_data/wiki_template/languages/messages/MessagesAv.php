<?php
/** Avaric (авар)
 *
 * To improve a translation please visit https://translatewiki.net
 *
 * @ingroup Language
 * @file
 *
 */

$fallback = 'ru';

$specialPageAliases = array(
	'Activeusers'               => array( 'ХІаракатчилъи_бугел_гІахьалчагІи' ),
	'Allmessages'               => array( 'Системаялъулал_баян_кьеял' ),
	'AllMyUploads'              => array( 'Киналго_дир_файлал' ),
	'Allpages'                  => array( 'Киналго_гьумерал' ),
	'Badtitle'                  => array( 'БукІине_бегьулареб_цІар' ),
	'Blankpage'                 => array( 'ЧІобогояб_гьумер' ),
	'Block'                     => array( 'Блокалада_лъезе' ),
	'Booksources'               => array( 'ТІахьазул_иццал' ),
	'BrokenRedirects'           => array( 'Рек-рекарал_цоги_бакІалде_руссинариял' ),
	'Categories'                => array( 'Категориял' ),
	'ChangeEmail'               => array( 'e-mail_хисизе', 'Почта_хисизе' ),
	'ChangePassword'            => array( 'Балъгояб_рагІи_хисизе' ),
	'ComparePages'              => array( 'Гьумеразул_дандекквей' ),
	'Confirmemail'              => array( 'E-mail_битІухъ_гьаби', 'почта_битІухъ_гьаби' ),
	'Contributions'             => array( 'Хазина' ),
	'CreateAccount'             => array( 'Учёталъулаб_Хъвай-хъвагІай_гІуцІцІизе', 'ГІахьалчи_гІуцІцІизе', 'Регистрация_гьабизе' ),
	'Deadendpages'              => array( 'Нух_къарал_гьумерал' ),
	'DeletedContributions'      => array( 'Нахъе_гьабураб_хазина' ),
	'Diff'                      => array( 'Хиса-басиял' ),
	'DoubleRedirects'           => array( 'КІицІулго_цоги_бакІалде_руссинариял' ),
	'EditWatchlist'             => array( 'Халкквеялъул_сияхІ_хисизабизе' ),
	'Emailuser'                 => array( 'ГІахьалчиясухъе_кагъат', 'Кагъат_битІизе' ),
	'ExpandTemplates'           => array( 'Шаблонал_кколе-кколелъуре_ккезари' ),
	'Export'                    => array( 'КъватІибе_битІи', 'ЧIехьей' ),
	'Fewestrevisions'           => array( 'КъанагІат_хиса-баси_гьарулел' ),
	'FileDuplicateSearch'       => array( 'Релъарал_файлал_хъирщи' ),
	'Filepath'                  => array( 'Файлалде_нух' ),
	'Import'                    => array( 'Импорт' ),
	'Invalidateemail'           => array( 'Адрес_битІухъ_гьаби_нахъ_чІвазе' ),
	'JavaScriptTest'            => array( 'JavaScript_хІалбихьи' ),
	'BlockList'                 => array( 'Блокалда_лъеялъул_сияхІ', 'Блокалда_лъеял' ),
	'LinkSearch'                => array( 'Ссылкаби_хъирщи' ),
	'Listbots'                  => array( 'Ботазул_сияхІ' ),
	'Listfiles'                 => array( 'Файлазул_сияхІ', 'Суратазул_сияхІ' ),
	'Listgrouprights'           => array( 'ГІахьалчагІазул_группабазул_ихтиярал', 'Группабазул_ихтияразул_сияхІ' ),
	'Listredirects'             => array( 'Цоги_бакІалде_руссинабиязул_сияхІ' ),
	'ListDuplicatedFiles'       => array( 'Релъарал_файлазул_сияхІ' ),
	'Listusers'                 => array( 'ГІахьалчагІазул_сияхІ' ),
	'Lockdb'                    => array( 'ХІБ_блокалда_лъезе', 'ХІужжабазул_база_блокалда_лъезе' ),
	'Log'                       => array( 'Журналал', 'Журнал' ),
	'Lonelypages'               => array( 'БатІатІурал_гьумерал' ),
	'Longpages'                 => array( 'Халатал_гьумерал' ),
	'MergeHistory'              => array( 'Тарихал_цо_гьари' ),
	'MIMEsearch'                => array( 'MIME_ялдалъул_хъирщи' ),
	'Mostcategories'            => array( 'Бищунго_категориял_цІикІкІарал' ),
	'Mostimages'                => array( 'Бищунго_хІалтІизарулел_файлал' ),
	'Mostinterwikis'            => array( 'Интервики-ссылкабазул_бищун_цІикІкІараб_къадар' ),
	'Mostlinked'                => array( 'Бищунго_хІалтІизарулел_гьумерал' ),
	'Mostlinkedcategories'      => array( 'Бищунго_хІалтІизарулел_категориял' ),
	'Mostlinkedtemplates'       => array( 'Бищунго_хІалтІизарулел_шаблонал' ),
	'Mostrevisions'             => array( 'Сверелазул_бищун_цІикІкІараб_къадар' ),
	'Movepage'                  => array( 'Гьумералда_цІар_хисизабизе', 'ЦІар_хисизаби', 'ЦІар_хисизе' ),
	'Mycontributions'           => array( 'Дир_хазина' ),
	'MyLanguage'                => array( 'Дир_мацІ' ),
	'Mypage'                    => array( 'Дир_гьумер' ),
	'Mytalk'                    => array( 'Дир_бахІс' ),
	'Myuploads'                 => array( 'Дица_жанире_цІарал_жал' ),
	'Newimages'                 => array( 'ЦІиял_файлал' ),
	'Newpages'                  => array( 'ЦІиял_гьумерал' ),
	'PasswordReset'             => array( 'Сброс_пароля' ),
	'PermanentLink'             => array( 'Даимаб_ссылка' ),
	'Preferences'               => array( 'Рекъезабиял' ),
	'Prefixindex'               => array( 'ЦІаразул_бетІералде_бихьизаби' ),
	'Protectedpages'            => array( 'ЦІунарал_гьумерал' ),
	'Protectedtitles'           => array( 'ЦІунарал_цІарал' ),
	'Randompage'                => array( 'Цебе_ккараб_гьумер', 'Цебе_ккараб' ),
	'Randomredirect'            => array( 'Цебе_ккараб_цоги_бакІалде_руссинаби' ),
	'Recentchanges'             => array( 'ЦІиял_хиса-басиял' ),
	'Recentchangeslinked'       => array( 'Хурхинарурал_хиса-басиял' ),
	'Revisiondelete'            => array( 'Хиса-баси_нахъе_бацІцІи' ),
	'Search'                    => array( 'Хъирщи' ),
	'Shortpages'                => array( 'Къокъал_гьумерал' ),
	'Specialpages'              => array( 'Хассал_гьумерал' ),
	'Statistics'                => array( 'Статистика' ),
	'Tags'                      => array( 'ГІужал' ),
	'Unblock'                   => array( 'Блокалдаса_бахъи' ),
	'Uncategorizedcategories'   => array( 'Категориял_гьечІел_категориял' ),
	'Uncategorizedimages'       => array( 'Категориял_гьечІел_файлал' ),
	'Uncategorizedpages'        => array( 'Категориял_гьечІел_гьумерал' ),
	'Uncategorizedtemplates'    => array( 'Категориял_гьечІе_шаблонал' ),
	'Undelete'                  => array( 'ТІадбуссинабизе', 'ТІадбуссинаби' ),
	'Unlockdb'                  => array( 'ХІБ_блокалдаса_бахъи' ),
	'Unusedcategories'          => array( 'ХІалтІизаруларел_категориял' ),
	'Unusedimages'              => array( 'ХІалтІизаруларел_файлал' ),
	'Unusedtemplates'           => array( 'ХІалтІизаруларел_шаблонал' ),
	'Upload'                    => array( 'Загрузка' ),
	'UploadStash'               => array( 'Бахчараб_загрузка' ),
	'Userlogin'                 => array( 'Жаниве_лъугьин' ),
	'Userlogout'                => array( 'Сеанс_лъугІи', 'КъватІиве_лъугьин' ),
	'Userrights'                => array( 'Ихтиярал_рилълъинари' ),
	'Version'                   => array( 'Сверел', 'Версия' ),
	'Wantedcategories'          => array( 'ХІажатал_категориял' ),
	'Wantedfiles'               => array( 'ХІажатал_файлал' ),
	'Wantedpages'               => array( 'ХІажатал_гьумерал' ),
	'Wantedtemplates'           => array( 'ХІажатал_шаблонал' ),
	'Watchlist'                 => array( 'Халкквеялъул_сияхІ' ),
	'Whatlinkshere'             => array( 'Ссылкаби_гьанире' ),
	'Withoutinterwiki'          => array( 'Интервики_гьечІого' ),
);