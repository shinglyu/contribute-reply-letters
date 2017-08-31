# mailer.py is auto-generated from templates, please edit template_*.jinja.py
# files instead.
contents = {
    
        '_header': '''Hi {%name%},  我們是 Mozilla 台灣社群

歡迎您加入 Mozilla 社群的大家族。Mozilla 是為維護網路的自由與創新的非營利組織，也是 Firefox 的開發者，更是一群愛好網路的人。
如果您想要更加了解 Mozilla，推薦您觀看以下五部短片： http://bit.ly/1kJmLV4

我們台灣社群*1 為了支持與實踐 Mozilla 宣言*2，而聚集在一起付出與學習。
我們的主要任務是推廣相關理念，以及正體中文在地化工作（Firefox 及 Mozilla 相關軟體、網站的正體中文翻譯）。
*1 MozTW  https://moztw.org
*2 Mozilla 宣言  http://www.mozilla.org/zh-TW/about/manifesto/

此頁條列整理了社群的日常工作、及需要各位貢獻的項目，歡迎查看，並且將您有興趣的部分告知我們： https://moztw.org/contribute
也歡迎加入我們的線上聊天頻道：  http://moztw.org/tg   (moztw 頻道)

如果您來自香港，我們在此也向您推介介紹香港 Mozilla 社群，歡迎看看以下幾個推廣及集人氣的 Facebook 頁面：http://fb.me/mozillahk、http://fb.me/firefoxhk
香港社群不定期會舉行一些社群聚會，到時歡迎來聊聊啊。 
''',
    
        '_footer': '''請先看看你對什麼比較有興趣，然後回信告訴我們，我們可以協助您更深入了解。

此外，也邀請您加入以下溝通頻道，與其他對 Mozilla 開發感興趣的朋友互相交流。
* Mozilla 中文開發者郵件群組  ( https://lists.mozilla.org/listinfo/dev-general-zh )
* MozTW dev/add-on Telegram 頻道  ( https://moztw.org/tg )

關於開發方面的問題也歡迎上 irc.mozilla.org 的 #mozilla-taiwan 頻道發問，有不少 Mozilla 台灣分公司的工程師與社群成員常駐。

最後，MozTW 社群目前每週五晚上 7:30，在台北有個咖啡小聚，如果您時間上允許，也歡迎來當面跟我們聊聊，地點詳情在此： http://moztw.org/events/moztw-lab/


MozTW, Mozilla 台灣社群
''',
    
        'support': '''=== 使用者支援 ===

Hi,  我是 Mozilla 台灣社群的 Ernest。

# 在論壇協助回答問題

在討論區協助回答問題，是最快速又簡單的參與方式。MozTW 的討論區每天都有各式各樣的問題，你可以指引出能提供協助的網頁、或者直接回答問題，來協助 Firefox 的用戶們。一起來分享你的 Firefox 知識吧！

- 討論區 Firefox 版：http://forum.moztw.org/viewforum.php?f=2
- 討論區 Thunderbird 版：http://forum.moztw.org/viewforum.php?f=9
- Ptt Browser 版


# 翻譯 SUMO 支援文件

Mozilla 主要是透過翻譯 SUMO 技術支援網站來提供 Firefox 用戶支援。SUMO 是 SUpport MOzilla (support.mozilla.org) 的縮寫，提供 Mozilla 產品各語言的使用教學、疑難排解、Q&A 等資訊。使用者只要按下 Firefox 的「說明」→「Firefox 說明」，就會連結到 SUMO 網站。

- 平均翻譯 1 篇 SUMO 文章，每天就可以幫助到中文世界的 1000 個用戶喔！
- SUMO 的貢獻方式，請先閱讀本份簡報：SUMO 網站翻譯流程 https://www.slideshare.net/dwchiang/moztw-about-sumo-20140315
- 並請參考「Firefox 說明文件在地化」一文：https://support.mozilla.org/zh-TW/kb/localize-firefox-help
- 建議從以下最多人閱讀的文章，開始翻譯與更新的工作：https://support.mozilla.org/zh-TW/localization#most-visited-translations（黃燈和紅燈優先）


# Army of Awesome

你還可以在線上透過「小莎的好厲害大軍 (Army of Awesome)」系統，即時回覆 Twitter 上的 Firefox 相關問題。
請參照「徵求超人義工」文中說明： https://support.mozilla.org/zh-TW/kb/superheroes-wanted
''',
    
        'qa': '''=== QA 測試專案 ===

Hi,  我是 Mozilla 台灣社群的 Toby

Mozilla QA 團隊是一個分散在全球各地的社群，協助測試早期產品、新功能、回報 Bug、撰寫執行 test case 與自動化測試，並從可用性的角度提供建議。

你可以在以下頻道上追蹤 QA 團隊最新資訊：

- QMO 網站 https://quality.mozilla.org/
- Facebook  https://www.facebook.com/pages/Mozilla-QA/122167964300
- Twitter  https://twitter.com/mozillaqa


# 保持聯繫

Mozilla QA 團隊的主要聯絡管道（英文為主）有以下數個：

- IRC  irc.mozilla.org #qa 頻道

IRC 是一種線上聊天系統，詳細說明請看： https://wiki.mozilla.org/IRC

- 郵件群組

當你加入郵件群組後，就會開始收到群組中其他人的信件，也可以回信與他人共同討論： http://groups.google.com/group/mozilla.dev.quality/

- Discourse

你也可以到 Discourse 上留言與參與討論： https://discourse.mozilla-community.org/c/quality-assurance

使用測試版軟體

貢獻 QA 專案最簡單的方法是在日常生活中使用全系列的 Nightly 版軟體，並在發現問題時到 Bugzilla 回報 Bug。

# Firefox 桌面版 & Android 版

Firefox 有四個開發頻道，這是相關說明： http://mozlinks-zh.blogspot.com/2012/12/firefox_5.html

請在此下載桌面與 Android 的 Firefox Nightly 測試版，並協助回報 Bug： http://nightly.mozilla.org/

- 擴充套件相容性測試

歡迎安裝 Add-on Compatibility Reporter 套件，協助回報與新版 Firefox 不相容的套件：  https://addons.mozilla.org/zh-tw/firefox/addon/add-on-compatibility-reporter/

- 擴充套件編輯團隊

如果您有套件的開發經驗，可以加入 Addon Editors 協助審核跟編輯套件精選： https://wiki.mozilla.org/AMO:Editors

- Test Pilot

您可以在桌面版 Firefox 上安裝 Test Pilot 套件，協助測試 Firefox 的開發中未來新功能： https://testpilot.firefox.com/

- MozTrap

在 MozTrap 上有很多設計好的測試，歡迎參照說明一一進行：
  https://moztrap.mozilla.org/results/runs/

- MDN

MDN 上有很多 QA 相關的技術文件，可供參考：
 https://developer.mozilla.org/zh-TW/docs/Mozilla/QA


# Firefox for iOS

你可以在此網站登記參加 iOS 版 Firefox 的測試：  https://www.mozilla.org/en-US/firefox/ios/testflight/


# Firefox 與 Thunderbird 中文討論區

當您有空也可以幫忙看看 forum.moztw.org 上的 Firefox、Thunderbird 討論區，與 Ptt 的 Browser 版。當發現使用者有發現什麼 Bug 時，歡迎在 Telegram MozTW 頻道討論，或協助報上 Bugzilla。

- MozTW 討論區： https://forum.moztw.org
- 加入 Telegram 頻道： http://moztw.org/tg (moztw 頻道)


# 網頁 WebQA

WebQA 專案負責維護 Mozilla 各網站的品質，在此瞭解更多參與資訊：
https://quality.mozilla.org/teams/web-qa/

- WebQA 團隊的 IRC 頻道是 #mozwebqa

- 到 One and Done 上執行適合的工作   https://oneanddone.mozilla.org/team/6/

- 最適合新手試試的 exploratory testing   https://quality.mozilla.org/2012/11/exploratory-testing-on-moztrap-job-board-posting-1/

- 自動化測試的 MDN 文件： https://developer.mozilla.org/en-US/docs/Mozilla/QA/Running_Web_QA_automated_tests

- 自動化測試 Wiki  https://wiki.mozilla.org/QA/Execution/Web_Testing/Automation
''',
    
        'coding': '''=== Firefox ===

Hi, 我是 Kevin Hu，歡迎您貢獻 Firefox

Firefox 的基礎架構是 C/C++ / JS / XUL，只要了解 JS 或 CSS 就能幫 Firefox 除錯，在 Mozilla 寫軟體有蠻多面向可以選擇，例如你可以學習 Firefox 或 Thunderbird 的程式設計，主要以 C 或 C++ 為主。其實 Firefox Coding 並不難，對於剛起步的應該可以先從跑流程開始。兩個較大的挑戰是 build Firefox 與 hg version control system。


# 基本概念

您可以先參考以下介紹，了解基本概念：

Mozilla Links 正體中文版: 摩茲動手做（一）如何幫 Firefox 抓蟲
http://mozlinks-zh.blogspot.com/2012/02/firefox_25.html

這邊有每個步驟的詳細影片教學：http://codefirefox.com/
部分影片有中文字幕在此： https://www.youtube.com/watch?v=uQDVU1isiqs&index=1&list=PLWajH1udirHJ7dMP88G2OPgN_Uu5L0AuE


# Good First Bug

Mozilla 對於新手貢獻程式，有一個「Good First Bug」專案，一步步協助大家嘗試解決 Firefox 的第一個 bug，你可以上 Bugs Ahoy 系統，查詢你的專長面上，有哪些 Firefox 新手 Bug 可以挑戰：http://www.joshmatthews.net/bugsahoy/


=== Rust / Servo ===

# Rust

Rust 是 Mozilla 支持，社群主導的系統程式語言，跑得比光速還快、能在編譯時就預防記憶體錯誤、保證多執行緒時的資料安全性。
您可以在此下載安裝、閱讀文件與了解貢獻機會： http://rust-lang.org

這裡有台灣社群成員共同翻譯的 Rust 入門手冊： http://askeing.github.io/rust-book/
你可以在此參與社群定期聚會： http://rust-lang.tw


# Servo

Servo 是 Mozilla 以 Rust 開發的新瀏覽器引擎，更先進、更快，徹底的從根本的支援平行化、安全性、模組化、且特別考慮嵌入 (embedding) 等多元應用情境。

歡迎在此下載最新的 Nightly 版，並了解如何貢獻 Servo： https://servo.org

這裡整理出 Servo 初心者 issue 供您挑選： https://starters.servo.org
您若是對 Rust、HTML/CSS/JS (測試)或是 Python (CI/編譯環境)有興趣就可以輕鬆上手。


=== B2G OS ===

Boot to Gecko (B2G) 作業系統是一個社群維護的開源計畫，源自於 2011 年，目標是為 Open Web 建立一套完整獨立的作業系統。B2G 以 Linux 核心與 Gecko 成像引擎為基礎，被運用於商業的 Firefox OS 手機、與智慧型電視等產品。

目前社群正在執行一套轉移計畫，目標要讓 B2G 更加現代化，建立一個更為精簡的平台，並運用於智慧型電視及其他具潛力的連網裝置上。

如果您想要參與，歡迎參考下列頁面上的相關資訊： https://wiki.mozilla.org/B2G/Transition_Project/Call_For_Contribution#Chinese_.28Traditional.29_Version_.2F_.E6.AD.A3.E9.AB.94.E4.B8.AD.E6.96.87


=== 網頁開發 ===

MozTW 在 github ( https://github.com/moztw ) ，還有一些網頁、以及其他 HTML5/CSS3 的專案，是可以您可以著手幫忙的部分。Issue 中有一些網站相關的 Bug、與新功能的點子，等你一起來幫忙改。


=== 其他專案 ===

這裡提供一個 What Can I Do For Mozilla 的網站，能提示您哪一些 Mozilla 的專案能運用上你的程式技能，歡迎你試試： http://whatcanidoformozilla.org/

Mozilla 大多的專案也都有放到 Github 上，你可以在此探索有哪些可以貢獻的專案： https://github.com/mozilla
''',
    
        'marketing': '''=== 行銷專案 ===

Hi, 我是 Mozilla 社群的 Irvin。

在行銷與企劃方面，我們可提供您發揮的項目有以下幾項：


# 傳播資訊

請幫助我們幫助我們傳播 Firefox 的消息。請幫忙傳播以下網站上的資訊，到你的社群網站：

- MozTW 粉絲團  https://facebook.com/MozTW
- Mozilla Links 正體中文版  http://mozlinks.moztw.org/


# 抓火狐網站 http://gfx.tw

您可以在 MozTW 社群建立的「抓火狐」網站建立個人頁面，推薦你最喜歡的 Firefox 功能與套件，取得個人專屬推廣網址，並且貼上專屬貼紙。


# Active Mozilla

https://activate.mozilla.community/

Ａctive Mozilla 提供許多活動與宣傳計畫，讓你可以參考執行，協助行銷與推廣 Mozilla 的不同專案。


# 本地例行與推廣活動

MozTW 大約每一到兩個月舉行一次實體活動，例如各研討會設攤、Firefox 相關 Party、連續聚、推廣講座、紀錄片放映會……等等活動。您可以在這裡看到過去我們曾舉行過的活動：http://moztw.org/events/

我們的推廣活動企劃目標是具備社群風格的低成本、高歡樂的活動為主。例如某一年在 COSCUP 研討會上的設攤計畫（http://bit.ly/YsDdgw），結合實體與虛擬，宣傳 Android 版 Firefox 的同時也好玩。歡迎你一起參與活動的籌劃及執行，你也可以提出各種活動的點子，讓我們一起來實現。


# moztw.org 上的產品行銷與活動頁面

moztw.org 針對 Mozilla 產品會建立專屬的產品頁面，例如 Firefox（http://moztw.org/firefox）、Firefox Android（http://moztw.org/mobile ）。這些產品頁面的設計，需要志願者來收集資料、進行內容規劃，並且與網頁開發者合作開發，上線之後持續進行網頁的曝光度等分析。我們的網站每天大概都有 15k PV 左右，很適合作為學習網路行銷的好標的。相關工作歡迎大家來嘗試與學習。


# 社交網站行銷

MozTW 的 Facebook（http://www.facebook.com/MozTW）、Google+（http://plus.google.com/communities/110692367205504504391/）、Blog（http://mozlinks-zh.blogspot.com/）及 Foxmosa 的三個社交網站頻道（http://moztw.org/foxmosa），都是由社群成員所經營的管道，歡迎您加入來經營內容、也可以嘗試各種行銷的可能性。
''',
    
        'localization': '''=== 在地化專案 ===

嗨，我是 MozTW 的 Peter，很高興你有興趣加入我們，一起幫助 Mozilla 完善產品與網頁的在地化內容，在此將由我來協助你入門。

MozTW ( https://moztw.org/ ) 是 Mozilla 在台灣的社群，負責 Mozilla 產品的正體中文版本在地化與推廣。

Mozilla 目前有下列項目可以進行在地化：

# Mozilla 產品翻譯及網頁翻譯

- Mozilla 軟體

如：Firefox、Firefox for Android、Firefox for iOS、Thunderbird、Lightning、SeaMonkey

- Mozilla 網頁、介面部分

如：Mozilla 附加元件站（AMO）、Mozilla 開發者網路（MDN）、Mozilla 技術支援站（SUMO）

以上專案皆使用 Pontoon 平台翻譯內容，網址為： https://pontoon.mozilla.org/zh-TW/
登入後即可點擊任一專案開始翻譯的第一步！


# MDN、SUMO 的技術文章翻譯

在該平台登入後即可在網站內翻譯

MDN：https://developer.mozilla.org/zh-TW/
SUMO：https://support.mozilla.org/zh-TW/

建議您從最多人閱讀/點擊的文章開始翻譯，讓您的貢獻馬上有最大的效果。


# Mozilla Links 正體中文版也歡迎譯者與編輯加入

詳情請見：https://mozlinks-zh.blogspot.com/p/mozilla-links.html


您也可以參考 MozTW 翻譯站 https://translate.moztw.org/

各項 L10n 專案歡迎您直接下手，工作告一段落之後寫個信告訴我，我會不定時上去幫您的貢獻做最後調整與修改，再將其送出給 Mozilla。

如果遇到了任何問題或哪裡不清楚，或是卡關了需要幫助，非常歡迎您回信與我聯繫。

最後，祝您貢獻順利！
''',
    
        'webdev': '''=== 網站開發方面 ===

Hi,  我是 Mozilla 台灣社群的 Irvin。

網站開發方面，分為本地的社群網站 moztw.org 及 mozilla.org 旗下各專案，以下為您分別說明。


# Mozilla 各網站的開發資訊

這邊有 Mozilla 各專案的網站開發相關資訊，你可以參考你熟悉的語言，聯絡各專案負責人： https://wiki.mozilla.org/Webdev/GetInvolved

參與 Mozilla 國際上的網站開發，就從加入 IRC 聊天室開始吧。頻道是 #webdev。

http://mzl.la/irc_getting_started 是關於如何連上 IRC 的教學，而 http://mzl.la/webdev_irc 列出了一些網頁開發者會出沒的頻道。

如果您想要開始動手協助修改 Mozilla 網站：

- 請到 Bugzilla 創立一個帳號。Bugzilla 看起來有點不好用，請您先看看 http://mzl.la/bugzilla_for_humans （強烈建議您先看過這部 15 分鐘的影片）。

- 接下來，您可以到 https://wiki.mozilla.org/Webdev/GetInvolved 找個 WebDev 的 mentored bug，然後聯絡那個 bug 的師父 - 透過 IRC、email，或是在 bug 裡留言都可以。

- 最後，與您的師父一起，從 github 當中 fork 出該 bug 的頁面，您就可以開始練功打怪了。


# 台灣的社群計畫

MozTW 網站 http://moztw.org 是由社群所架設，提供 Firefox 等軟體下載及活動頁的網站，其下有 phpbb 系統的討論區，是繁中用戶討論發問的主要平台。以上 moztw.org 的總使用量，平均每個月約有 35~40 萬不重複訪客，90 萬 PV。

- 此網站及我們其他 HTML5 的專案，Repo 都放置在 https://github.com/moztw/ 上。網站是其中的 www.moztw.org Repo，您可以參考 readme，在本地端先架設測試站看看。

- 一些網站相關的 Bug、與新功能的點子都開在各 repo 的 issue 中，可以一起來幫忙改 https://github.com/moztw/www.moztw.org/issues

- 此外，社群還有一個「抓火狐」網站（ http://gfx.tw ） ，提供使用者自定推薦套件的 Firefox 產品頁活動網站。相關的 issue 也在 GitHub Repo 中：https://github.com/moztw/gfx.tw
''',
    
        'addons': '''=== 附加元件 ===

Hi,  我是 Mozilla 台灣社群的 Ettoolong

感謝您表達對 Firefox 附加元件的興趣，您很簡單就能開始貢獻，不論是為您最愛的附加元件留下評論、設計一個新的佈景主題、或是打造一套附加元件，您的貢獻都能幫到非常多忙！


# 推廣附加元件

若您是 Firefox 附加元件的新手，您可以到 https://addons.mozilla.org 做這些事:

- 為您最愛的附加元件留個言

到 https://addons.mozilla.org 搜尋您最愛的附加元件，然後到附加元件的詳情頁面，把畫面往下拉到留言區域，留下您的意見給開發者。

- 建立收藏集

收藏集讓您很簡單地就能追蹤您最愛的附加元件，並把您自訂好的瀏覽器分享給其他人。您可以從此處開始：
https://addons.mozilla.org/firefox/collections/


# 設計佈景主題

佈景主題讓您能自訂您 Firefox 的外觀。如果要建立您自己的佈景主題，請從此處下手：
https://developer.mozilla.org/en-US/Add-ons/Themes/Lightweight_themes


如果您更懂一點技術的東西，也可以試試下面幾件事

# 開發附加元件

請到附加元件開發者中心看看，那邊有開發文件、工具、以及如何與其他開發者交流的資訊：
https://addons.mozilla.org/developers/

目前 Firefox 上可以用 WebExtensions 來開發套件：
https://developer.mozilla.org/en-US/Add-ons/WebExtensions

用 WebExtensions 寫一個套件：
https://developer.mozilla.org/en-US/Add-ons/WebExtensions/Your_first_WebExtension

這邊有一些範例套件：
https://github.com/mdn/webextensions-examples

您也可以到附加元件討論區張貼問題，找到其他的附加元件開發者：
https://forums.mozilla.org/addons/

或在 MozTW 討論區擴充套件版，與其他華文的開發者與用戶進行交流：
http://forum.moztw.org/viewforum.php?f=11

# 幫助測試附加元件

若您有興趣測試附加元件，您可以加入 QA 品質檢測團隊：
http://quality.mozilla.org/

您也可以透過安裝 Add-on Compatibility Reporter 套件，透過傳送相容性報告，來協助回報與現有 Firefox 版本不相容的 Firefox 套件，幫助其他使用者與套件開發者：
https://addons.mozilla.org/firefox/addon/add-on-compatibility-reporter


# 貢獻附加元件社群

如果您有興趣協助參與 Mozilla 的 Add-on 開發與審核相關事務，歡迎參閱以下專案頁面：
https://wiki.mozilla.org/Add-ons/Contribute
''',
    
        'design': '''=== 美術設計專案 ===

Hi,  我是 Mozilla 台灣社群的 Irvin


# 參與創意團隊

目前 Mozilla 國際上的視覺設計由創意團隊負責，負責處理從圖示、行銷活動、網站設計等大大小小的專案。若您有興趣加入，以下是幾個您能幫忙的方式：

- 在 Twitter follow 創意團隊: http://www.twitter.com/mozcreative

- 創意團隊會在這邊張貼一些設計作品，但通常我們會把這個地方當作張貼與 Mozilla 的設計有關的主題的資訊頻道，當中也會有些啟發我們的設計。
到 wiki 看看其他資訊: http://wiki.mozilla.org/Design

- 您可以在 wiki 上找到各種可以參與貢獻的專案鏈結以及其他資源。內容將不定時更新，請記得常常回來看看。

- 此外，只要三個步驟，您就可以製作出 Firefox 的佈景主題，詳細說明於此: https://addons.mozilla.org/zh-TW/developers/docs/themes


# 本地的社群計畫

在 Mozilla 台灣社群這裡，目前設計與美術相關工作的重點，在網頁的美工跟 Foxmosa 相關的繪圖上。

歡迎透過此連結加入 MozTW Design 設計聊天頻道： http://moztw.org/tg ( MozTW Design)


- Foxmosa

Foxmosa 是我們的吉祥物，中文名稱是狐耳摩莎，暱稱小莎，這是她的個人網頁： http://moztw.org/foxmosa

Foxmosa 目前的主要插畫家有電腦君、Goescat…等人，在以下 PDF 中，我們彙整了這個角色一些過去的相關作品：
https://www.dropbox.com/s/js64y5e3sbhdjpu/foxmosa%20%E7%B9%AA%E5%B8%AB%E6%8B%9B%E5%8B%9F.pdf

MozTW 歡迎你自由以 Foxmosa 這個角色為主題來創作，唯一的限制是你的作品需要與大家自由分享，且不能有商業應用。（請採用創用 CC 姓名標示-非商業性-相同方式分享-3.0 TW 授權釋出）


# 網頁及平面美工

http://moztw.org 網站內所有圖片、舉辦活動時的頁面圖畫（例如 Party、年節賀卡……），以及實體海報等等，均需要各位來協助繪製，不定期會有相關需求。

如果您有興趣，請回信告知，並加入 Telegram 上的設計聊天室（ http://moztw.org/tg 選擇 "設計" 頻道），在需要繪圖時，我們就會以上管道討論。

- 例如以下兩張我們參加全球年會時的海報：
https://www.dropbox.com/s/6r37jit1dxjsxld/Mozilla%20summit%202010%20MozTW.png
https://www.dropbox.com/s/li0aickd9epodzm/Mozilla%20summit%202010%20Taiwan.png

- 以及先前的瀏覽器歷史海報（由 Mozilla 與 Mozilla Japan 製作，我們進行翻譯）：
瀏覽器歷史 2012 https://www.dropbox.com/s/d0lfm5g61lvytjh/2012_history-foxmosa-A3_zh-tw-90x120.png
''',
    
        'documentation': '''=== 文件支援專案 ===

Hi, 我是 MozTW 社群的 Irvin

Mozilla 有兩個主要的文件專案：SUMO「Mozilla 技術支援」及 MDN「Mozilla 開發者社群」。以下為您說明兩者的參與方式與管道。


# SUMO

http://support.mozilla.org

SUMO 是 SUpport MOzilla 的縮寫，提供 Mozilla 產品各語言的使用教學、疑難排解、Q&A 等資訊。使用者只要按下 Firefox 的「說明」→「Firefox 說明」，就會連結到 SUMO 網站。

我們主要透過翻譯 SUMO 技術支援網站，來提供 Firefox 用戶支援。
平均翻譯 1 篇 SUMO 文章，每天就可以幫助到中文世界的 1000 個用戶喔！

- SUMO 的貢獻方式，請先閱讀本份簡報：SUMO 網站翻譯流程 http://www.slideshare.net/dwchiang/translation-process-for-sumo-new-website-zhtw-201305

- 並請參考「Firefox 說明文件在地化」一文：https://support.mozilla.org/zh-TW/kb/localize-firefox-help

- 建議從以下最多人閱讀的文章，開始翻譯與更新的工作（黃燈和紅燈優先）：https://support.mozilla.org/zh-TW/localization#most-visited-translations

- 您也可以撰寫新的補助說明文章，步驟與指引請參考本文：https://support.mozilla.org/zh-TW/kb/improve-knowledge-base


# MDN

http://developer.mozilla.org/

MDN（Mozilla Developer Network, Mozilla 開發者社群）是網路創作者的社群平台，只要是網路開發者，不論使用的是任何語言或軟體，都可以在這裡查詢到相關的技術文件與範例，MDN 的目標是要成為網路上最好的開發文件中心。

- 編寫技術文件

MDN 的內容包含 HTML/CSS/JS 等語言參考，及 DOM、Gecko、Web API、Firefox……等技術文件，是一個 wiki 架構的網站，任何頁面都可以直接編輯與翻譯。

1. 請註冊帳號並且登入網站：https://developer.mozilla.org/
2. 瀏覽英文版 MDN （ http://developer.mozilla.org/en-US/ ），找到您想翻譯的文章後，在右上角的 Language 選單下拉，選擇「Add translation」，選擇「正體中文 (繁體) (zh-TW)」。
3. 根據左邊的英文原文，在右方進行中文翻譯。
4. 將文章標題（Title）修改為中文。網址（Slug）則不動。
6. 翻譯時，請力求流暢。文中使用到標點符號請用全形「，；。、……」，中英文字間請加一個半形空白較美觀。

請參考最熱門的文章列表，優先對這些文章進行翻譯： https://developer.mozilla.org/Special:Popularpages

也請參閱以下說明文章：
MDN:如何協助    https://developer.mozilla.org/zh-TW/docs/Project:How_to_Help
Getting Started    https://developer.mozilla.org/zh-TW/docs/Project:Getting_started
Formatting Guide   https://developer.mozilla.org/zh-TW/docs/Project:MDC_style_guide


# Mozilla Links 正體中文版

如果您有興趣撰寫、翻譯中文的 Firefox 教學文章、報導或新聞，歡迎加入 Mozilla Links 正體中文版專案

詳情請參閱編輯機動隊說明： http://mozlinks-zh.blogspot.com/p/mozilla-links.html
''',
    
        'education': '''=== 教育專案 ===

Hi!

我是 Mozilla 台灣社群的柏強（BobChao），在此感謝您表達對於 Mozilla 與教育相關專案的興趣。

Mozilla 在教育方面，提出了「Webmaker」專案。我們希望協助眾人提升 Web 素養 https://webmaker.org/zh-TW/standard，也非常需要您的協助。


# 先玩玩看！

Webmaker 是與 Web 教育相關的專案，強調動手做精神。請先試試看我們提供的工具，這些工具可以協助您查看網頁背後的原理、編撰網路上的多媒體資訊，甚至簡單打造自己的網頁：https://webmaker.org/zh-TW/tools


# 想開始傳授 Web 知識了嗎？

一份規劃好的教案對教學很有幫助，我們的全球社群已經撰寫了許多教案，您可以先從自己的親人、朋友、鄰居做起，試著協助他們認識 Web：https://webmaker.org/zh-TW/teach


# 更進一步：成為 Webmaker 輔導員

如果您對協助他人學習感興趣，歡迎前往 Webmaker 輔導員頁面，並根據其中資訊，加入全球數百位輔導員的行列：https://webmaker.org/zh-TW/mentor


# 參與活動討論，與夥伴碰面

Mozilla 台灣社群（MozTW）是一群跟您一樣熱愛網路的人，歡迎您加入，認識志同道合的夥伴彼此砥礪：

- 您可以先從線上討論區開始參與 https://groups.google.com/group/moztw-general (記得先自我介紹喲！)
- 也歡迎加入我們的 Telegram 線上即時聊天頻道 https://moztw.org/tg  (MozTW)
- 我們經常有實體聚會與活動，包括每週於各地舉辦的 MozTW Lab，地點詳情請見 http://moztw.org/events/moztw-lab/


總之，再次歡迎您的加入；有您的參與，維護網路創新與選擇的 Mozilla 就能更有力量 :)
''',
    
        'suggestions': '''=== 意見回饋 ===

感謝您有興趣提供 Firefox 的意見回饋。
建議您可以切換使用下一版 Firefox 的預覽版本，試試看我們努力打造，即將在未來會推出的新功能。您可以在下列位置下載：
http://www.mozilla.com/firefox/channel/

試用完之後，歡迎您到下列網址分享您的感想：
https://input.mozilla.org/zh-TW/feedback

也歡迎到台灣社群的線上頻道聊聊，加入之後記得自介喔：
http://moztw.org/tg (moztw 頻道)
''',
    
        'issues': '''=== 疑難求助 ===

Hi, 我是 Mozilla 台灣社群的 Irvin，很抱歉您使用 Firefox 的時候遇到了問題。

- 我們建議您可以先到 Firefox 技術支援網站，搜索看看有沒有相關的說明文件：
  https://support.mozilla.org

- 另外您也可以試試重置您的 Firefox，可以解決許多問題：
  https://support.mozilla.org/zh-TW/kb/reset-firefox/

- 也請您到此檢查你的 Firefox 與外掛元件是否已經更新到最新版本：
  https://www.mozilla.org/en-US/firefox/update/
  https://www.mozilla.org/zh-TW/plugincheck/

- 如果以上還沒有辦法解決您的問題，您還可以到 MozTW Firefox 討論區發問，那邊有一群專家網友可以幫助您解決問題：
  http://forum.moztw.org/viewforum.php?f=2

如果還有其他問題，歡迎直接回信給我們，我們非常樂意協助你。謝謝！
''',
    
        'other': '''=== 其他 ===

Hi, 我是 Mozilla 台灣社群的 Irvin。

歡迎你先逛逛我們的 Facebook ( http://fb.me/moztw )、Blog ( http://mozlinks-zh.blogspot.com/ ) 及 Foxmosa 的社交頻道（ http://moztw.org/foxmosa/#foxmosa-social ），這些都是由社群成員所經營的內容，希望能讓你更為了解我們在做些什麼。
''',
    
}

# Depends on src/email_contents.py
def format_body(name, interests):
    body = []

    # TODO: we should probably use some template solution
    
    body.append(contents['_header'].replace('{%name%}', name))
    

    for interest in interests:
        body.append(contents[interest])

    body.append(contents['_footer'])

    return '\n'.join(body)

import json
import boto3

ses = boto3.client('ses')

def lambda_handler(event, context):
    
    email_from = 'contribute@moztw.org'
    # email_to = 'CHANGE_ME'
    email_cc = email_from
    email_subject = 'Hello from Mozilla'
    # email_body = 'Hello '

    #print("Received event: " + json.dumps(event, indent=2))
    print("name = " + event['name'])
    print("email = " + event['email'])
    print("interests = " + str(event['interests']))
    # print("value3 = " + event['key3'])
    # return event['key1']  # Echo back the first key value
    #raise Exception('Something went wrong')
    send_email(ses,
               email_from,
               event['email'],
               email_cc,
               email_subject,
               format_body(event['name'], event['interests']))


def send_email(ses_service, email_from, email_to, email_cc, subject, body):
    response = ses_service.send_email(
        Source = email_from,
        Destination={
            'ToAddresses': [
                email_to,
            ],
            'CcAddresses': [
                email_cc,
            ]
        },
        Message={
            'Subject': {
                'Data': subject
            },
            'Body': {
                'Text': {
                    'Data': body
                }
            }
        }
    )