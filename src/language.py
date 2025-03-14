## You can edit & add new translations!
## 34 language supported!

def translate(lang: str, key: str) -> str:
    """Return traslation: print(translate(current_lang, 'greeting'))"""
    return translations.get(lang, {}).get(key, translations['en'].get(key, key))

all_language = """[ru] - Русский
[en] - English
[es] - Español
[fr] - Français
[de] - Deutsch
[nl] - Nederlands
[it] - Italiano
[sv] - Svenska
[da] - Dansk
[no] - Norsk
[pl] - Polski
[cs] - Čeština
[sk] - Slovenčina
[sr] - Српски / Srpski
[bg] - Български
[hu] - Magyar
[el] - Ελληνικά
[fi] - Suomi
[tr] - Türkçe
[pt] - Português
[sq] - Shqip
[ka] - ქართული
[eo] - Esperanto
[fa] - فارسی 
[uz] - Oʻzbekcha
[mn] - Монгол
[he] - עברית
[ar] - العربية
[ko] - 한국어
[hi] - हिन्दी
[bn] - বাংলা
[vi] - Tiếng Việt
[zh] - 中文
[ja] - 日本語"""

translations = {
    ## English
    'en': {
        'commands': 'Commands:',
        'enter_button': 'Input your command:',
        'change_lang': 'Change language',
        'wid_hei_bx': '[width] [height] - Change box size',
        'num_of_gen': '[number] - Number of generations',
        'start': 'Start Cell Automaton',
        'end': 'End of generations',
        'enter': 'Press Enter to continue',
        'gen': 'Generation:',
        'choice_lang': 'Select supported language:',
        'example_lang': 'Example: input "en" for English'
    },

    ## Russian
    'ru': {
        'commands': 'Команды:',
        'enter_button': 'Введите команду:',
        'change_lang': 'Сменить язык',
        'wid_hei_bx': '[ширина] [высота] - Изменить размер области',
        'num_of_gen': '[число] - Количество поколений',
        'start': 'Запустить клеточный автомат',
        'end': 'Конец генераций',
        'enter': 'Нажмите Enter для продолжения',
        'gen': 'Поколение:',
        'choice_lang': 'Выберите язык:',
        'example_lang': 'Пример: введите "ru" для русского'
    },

    ## Spanish
    'es': {
        'commands': 'Comandos:',
        'enter_button': 'Ingrese comando:',
        'change_lang': 'Cambiar idioma',
        'wid_hei_bx': '[ancho] [alto] - Cambiar tamaño',
        'num_of_gen': '[número] - Número de generaciones',
        'start': 'Iniciar autómata celular',
        'end': 'Fin de generaciones',
        'enter': 'Presione Enter para continuar',
        'gen': 'Generación:',
        'choice_lang': 'Seleccione idioma:',
        'example_lang': 'Ejemplo: ingrese "es" para español'
    },

    ## French
    'fr': {
        'commands': 'Commandes:',
        'enter_button': 'Saisir commande:',
        'change_lang': 'Changer de langue',
        'wid_hei_bx': '[largeur] [hauteur] - Modifier taille',
        'num_of_gen': '[nombre] - Nombre de générations',
        'start': 'Démarrer automate cellulaire',
        'end': 'Fin des générations',
        'enter': 'Appuyez sur Entrée',
        'gen': 'Génération:',
        'choice_lang': 'Choisir langue:',
        'example_lang': 'Exemple: "fr" pour français'
    },

    ## German
    'de': {
        'commands': 'Befehle:',
        'enter_button': 'Befehl eingeben:',
        'change_lang': 'Sprache ändern',
        'wid_hei_bx': '[Breite] [Höhe] - Größe ändern',
        'num_of_gen': '[Anzahl] - Generationen',
        'start': 'Zellularautomat starten',
        'end': 'Ende der Generationen',
        'enter': 'Enter drücken',
        'gen': 'Generation:',
        'choice_lang': 'Sprache wählen:',
        'example_lang': 'Beispiel: "de" für Deutsch'
    },

    ## Dutch
    'nl': {
        'commands': 'Commando\'s:',
        'enter_button': 'Voer opdracht in:',
        'change_lang': 'Taal wijzigen',
        'wid_hei_bx': '[breedte] [hoogte] - Grootte wijzigen',
        'num_of_gen': '[aantal] - Aantal generaties',
        'start': 'Start cellulaire automaat',
        'end': 'Einde generaties',
        'enter': 'Druk op Enter',
        'gen': 'Generatie:',
        'choice_lang': 'Selecteer taal:',
        'example_lang': 'Voorbeeld: "nl" voor Nederlands'
    },

    ## Italian
    'it': {
        'commands': 'Comandi:',
        'enter_button': 'Inserisci comando:',
        'change_lang': 'Cambia lingua',
        'wid_hei_bx': '[larghezza] [altezza] - Modifica dimensione',
        'num_of_gen': '[numero] - Numero di generazioni',
        'start': 'Avvia automa cellulare',
        'end': 'Fine generazioni',
        'enter': 'Premi Invio',
        'gen': 'Generazione:',
        'choice_lang': 'Seleziona lingua:',
        'example_lang': 'Esempio: "it" per italiano'
    },

    ## Swedish
    'sv': {
        'commands': 'Kommandon:',
        'enter_button': 'Ange kommando:',
        'change_lang': 'Ändra språk',
        'wid_hei_bx': '[bredd] [höjd] - Ändra storlek',
        'num_of_gen': '[antal] - Antal generationer',
        'start': 'Starta cellautomat',
        'end': 'Slut på generationer',
        'enter': 'Tryck Enter',
        'gen': 'Generation:',
        'choice_lang': 'Välj språk:',
        'example_lang': 'Exempel: "sv" för svenska'
    },

    ## Danish
    'da': {
        'commands': 'Kommandoer:',
        'enter_button': 'Indtast kommando:',
        'change_lang': 'Skift sprog',
        'wid_hei_bx': '[bredde] [højde] - Ændr størrelse',
        'num_of_gen': '[antal] - Antal generationer',
        'start': 'Start celleautomat',
        'end': 'Slut på generationer',
        'enter': 'Tryk Enter',
        'gen': 'Generation:',
        'choice_lang': 'Vælg sprog:',
        'example_lang': 'Eksempel: "da" for dansk'
    },

    ## Norwegian
    'no': {
        'commands': 'Kommandoer:',
        'enter_button': 'Skriv inn kommando:',
        'change_lang': 'Bytt språk',
        'wid_hei_bx': '[bredde] [høyde] - Endre størrelse',
        'num_of_gen': '[antall] - Antall generasjoner',
        'start': 'Start celleautomat',
        'end': 'Slutt på generasjoner',
        'enter': 'Trykk Enter',
        'gen': 'Generasjon:',
        'choice_lang': 'Velg språk:',
        'example_lang': 'Eksempel: "no" for norsk'
    },

    ## Polish
    'pl': {
        'commands': 'Polecenia:',
        'enter_button': 'Wprowadź polecenie:',
        'change_lang': 'Zmień język',
        'wid_hei_bx': '[szerokość] [wysokość] - Zmień rozmiar',
        'num_of_gen': '[liczba] - Liczba generacji',
        'start': 'Uruchom automat komórkowy',
        'end': 'Koniec generacji',
        'enter': 'Naciśnij Enter',
        'gen': 'Generacja:',
        'choice_lang': 'Wybierz język:',
        'example_lang': 'Przykład: "pl" dla polskiego'
    },

    ## Czech
    'cs': {
        'commands': 'Příkazy:',
        'enter_button': 'Zadejte příkaz:',
        'change_lang': 'Změnit jazyk',
        'wid_hei_bx': '[šířka] [výška] - Změnit velikost',
        'num_of_gen': '[číslo] - Počet generací',
        'start': 'Spustit buněčný automat',
        'end': 'Konec generací',
        'enter': 'Stiskněte Enter',
        'gen': 'Generace:',
        'choice_lang': 'Vyberte jazyk:',
        'example_lang': 'Příklad: "cs" pro češtinu'
    },

    ## Slovak
    'sk': {
        'commands': 'Príkazy:',
        'enter_button': 'Zadajte príkaz:',
        'change_lang': 'Zmeniť jazyk',
        'wid_hei_bx': '[šírka] [výška] - Zmeniť veľkosť oblasti',
        'num_of_gen': '[číslo] - Počet generácií',
        'start': 'Spustiť bunkový automat',
        'end': 'Koniec generácií',
        'enter': 'Stlačte Enter pre pokračovanie',
        'gen': 'Generácia:',
        'choice_lang': 'Vyberte podporovaný jazyk zo zoznamu:',
        'example_lang': 'Príklad: zadajte "sk" pre slovenské rozhranie'
    },

    ## Serbian - Cyrillic
    'sr': {
        'commands': 'Команде:',
        'enter_button': 'Унесите команду:',
        'change_lang': 'Промени језик',
        'wid_hei_bx': '[ширина] [висина] - Промени величину',
        'num_of_gen': '[број] - Број генерација',
        'start': 'Покрени ћелијски аутомат',
        'end': 'Крај генерација',
        'enter': 'Притисните Enter за наставак',
        'gen': 'Генерација:',
        'choice_lang': 'Изаберите језик са списка:',
        'example_lang': 'Пример: унесите "sr" за српски интерфејс'
    },

    ## Bulgarian 
    'bg': {
        'commands': 'Команди:',
        'enter_button': 'Въведете команда:',
        'change_lang': 'Смени език',
        'wid_hei_bx': '[широчина] [височина] - Промяна на размера',
        'num_of_gen': '[число] - Брой поколения',
        'start': 'Стартирай клетъчен автомат',
        'end': 'Край на поколенията',
        'enter': 'Натиснете Enter',
        'gen': 'Поколение:',
        'choice_lang': 'Изберете език от списъка:',
        'example_lang': 'Пример: въведете "bg" за български интерфейс'
    },

    ## Hungarian
    'hu': {
        'commands': 'Parancsok:',
        'enter_button': 'Parancs bevitele:',
        'change_lang': 'Nyelv váltása',
        'wid_hei_bx': '[szélesség] [magasság] - Méret változtatása',
        'num_of_gen': '[szám] - Generációk száma',
        'start': 'Cellularis automata indítása',
        'end': 'Generációk vége',
        'enter': 'Nyomja meg az Entert',
        'gen': 'Generáció:',
        'choice_lang': 'Válasszon nyelvet a listából:',
        'example_lang': 'Például: írja be "hu" magyar nyelvhez'
    },

    ## Greek 
    'el': {
        'commands': 'Εντολές:',
        'enter_button': 'Εισαγωγή εντολής:',
        'change_lang': 'Αλλαγή γλώσσας',
        'wid_hei_bx': '[πλάτος] [ύψος] - Αλλαγή μεγέθους',
        'num_of_gen': '[αριθμός] - Αριθμός γενεών',
        'start': 'Εκκίνηση κυτταρικού αυτόματου',
        'end': 'Τέλος γενεών',
        'enter': 'Πατήστε Enter',
        'gen': 'Γενιά:',
        'choice_lang': 'Επιλέξτε γλώσσα από τη λίστα:',
        'example_lang': 'Παράδειγμα: εισάγετε "el" για ελληνική διεπαφή'
    },

    ## Finnish
    'fi': {
        'commands': 'Komennot:',
        'enter_button': 'Syötä komento:',
        'change_lang': 'Vaihda kieltä',
        'wid_hei_bx': '[leveys] [korkeus] - Muuta laatikon kokoa',
        'num_of_gen': '[määrä] - Sukupolvien määrä',
        'start': 'Käynnistä soluautomaatti',
        'end': 'Sukupolvien loppu',
        'enter': 'Paina Enter jatkaaksesi',
        'gen': 'Sukupolvi:',
        'choice_lang': 'Valitse tuettu kieli listasta:',
        'example_lang': 'Esimerkiksi: syötä "fi" suomen kielelle'
    },

    ## Turkish 
    'tr': {
        'commands': 'Komutlar:',
        'enter_button': 'Komut girin:',
        'change_lang': 'Dili değiştir',
        'wid_hei_bx': '[genişlik] [yükseklik] - Kutu boyutunu değiştir',
        'num_of_gen': '[sayı] - Nesil sayısı',
        'start': 'Hücresel Otomat Başlat',
        'end': 'Nesil sonu',
        'enter': 'Devam etmek için Enter\'a basın',
        'gen': 'Nesil:',
        'choice_lang': 'Listeden desteklenen bir dil seçin:',
        'example_lang': 'Örneğin: "tr" yazın - Türkçe arayüz için'
    },

    ## Portuguese 
    'pt': {
        'commands': 'Comandos:',
        'enter_button': 'Insira seu comando:',
        'change_lang': 'Mudar idioma',
        'wid_hei_bx': '[largura] [altura] - Alterar tamanho da caixa',
        'num_of_gen': '[número] - Número de gerações',
        'start': 'Iniciar Autômato Celular',
        'end': 'Fim das gerações',
        'enter': 'Pressione Enter para continuar',
        'gen': 'Geração:',
        'choice_lang': 'Selecione um idioma da lista:',
        'example_lang': 'Exemplo: digite "pt" para português'
    },

    ## Albanian
    'sq': {
        'commands': 'Komandat:',
        'enter_button': 'Shkruaj komandën:',
        'change_lang': 'Ndrysho gjuhën',
        'wid_hei_bx': '[gjerësia] [lartësia] - Ndrysho madhësinë e kutisë',
        'num_of_gen': '[numri] - Numri i gjeneratave',
        'start': 'Nis Automatin Qelizor',
        'end': 'Fundi i gjeneratave',
        'enter': 'Shtyp Enter për të vazhduar',
        'gen': 'Gjenerata:',
        'choice_lang': 'Zgjidhni një gjuhë nga lista:',
        'example_lang': 'P.sh.: shkruani "sq" për shqip'
    },

    ## Georgian 
    'ka': {
        'commands': 'ბრძანებები:',
        'enter_button': 'შეიყვანეთ ბრძანება:',
        'change_lang': 'ენის შეცვლა',
        'wid_hei_bx': '[სიგანე] [სიმაღლე] - ყუთის ზომის შეცვლა',
        'num_of_gen': '[რიცხვი] - თაობების რაოდენობა',
        'start': 'უჯრედოვანი ავტომატის გაშვება',
        'end': 'თაობების დასასრული',
        'enter': 'გასაგრძელებლად დააჭირეთ Enter-ს',
        'gen': 'თაობა:',
        'choice_lang': 'აირჩიეთ ენა სიიდან:',
        'example_lang': 'მაგალითად: შეიყვანეთ "ka" ქართული ინტერფეისისთვის'
    },

    ## Esperanto 
    'eo': {
        'commands': 'Komandoj:',
        'enter_button': 'Enigu vian komon:',
        'change_lang': 'Ŝanĝi lingvon',
        'wid_hei_bx': '[larĝo] [alto] - Ŝanĝi skatolan grandecon',
        'num_of_gen': '[nombro] - Nombro de generacioj',
        'start': 'Starti ĉelan aŭtomaton',
        'end': 'Fino de generacioj',
        'enter': 'Premu Enter por daŭrigi',
        'gen': 'Generacio:',
        'choice_lang': 'Elektu subtenatan lingvon:',
        'example_lang': 'Ekzemple: enigu "eo" por Esperanto'
    },

    ## Persian/Farsi 
    'fa': {
        'commands': 'دستورات:',
        'enter_button': 'دستور خود را وارد کنید:',
        'change_lang': 'تغییر زبان',
        'wid_hei_bx': '[عرض] [ارتفاع] - تغییر اندازه جعبه',
        'num_of_gen': '[عدد] - تعداد نسل‌ها',
        'start': 'شروع اتومات سلولی',
        'end': 'پایان نسل‌ها',
        'enter': 'ادامه با Enter',
        'gen': 'نسل:',
        'choice_lang': 'زبان پشتیبانی شده انتخاب کنید:',
        'example_lang': 'مثال: "fa" را برای فارسی وارد کنید'
    },

    ## Uzbek
    'uz': {
        'commands': 'Buyruqlar:',
        'enter_button': 'Buyruq kiriting:',
        'change_lang': 'Tilni o\'zgartirish',
        'wid_hei_bx': '[eni] [balandligi] - Quti o\'lchamini o\'zgartirish',
        'num_of_gen': '[son] - Necha avlod',
        'start': 'Hujayrali avtomatni boshlash',
        'end': 'Avlodlar tugadi',
        'enter': 'Davom etish uchun Enter',
        'gen': 'Avlod:',
        'choice_lang': 'Ro\'yxatdan tilni tanlang:',
        'example_lang': 'Masalan: "uz" kiriting'
    },

    ## Mongolian - Cyrillic
    'mn': {
        'commands': 'Командууд:',
        'enter_button': 'Командаа оруулна уу:',
        'change_lang': 'Хэл солих',
        'wid_hei_bx': '[өргөн] [өндөр] - Хайрцгийн хэмжээ солих',
        'num_of_gen': '[тоо] - Үеийн тоо',
        'start': 'Эсний автомат эхлүүлэх',
        'end': 'Үеийн төгсгөл',
        'enter': 'Үргэлжлүүлэх Enter',
        'gen': 'Үе:',
        'choice_lang': 'Дэмжигдсэн хэлийг сонгоно уу:',
        'example_lang': 'Жишээ нь: "mn" оруулна уу'
    },

    ## Hebrew - RTL
    'he': {
        'commands': 'פקודות:',
        'enter_button': 'הזן פקודה:',
        'change_lang': 'שנה שפה',
        'wid_hei_bx': '[רוחב] [גובה] - שנה גודל תיבה',
        'num_of_gen': '[מספר] - מספר דורות',
        'start': 'התחל אוטומט תאים',
        'end': 'סוף הדורות',
        'enter': 'הקש Enter להמשך',
        'gen': 'דור:',
        'choice_lang': 'בחר שפה נתמכת:',
        'example_lang': 'לדוגמה: הקש "he" לעברית'
    },

    ## Arabic - RTL
    'ar': {
        'commands': 'الأوامر:',
        'enter_button': 'أدخل الأمر:',
        'change_lang': 'تغيير اللغة',
        'wid_hei_bx': '[العرض] [الارتفاع] - تغيير حجم الصندوق',
        'num_of_gen': '[العدد] - عدد الأجيال',
        'start': 'بدء الأوتومات الخلوي',
        'end': 'نهاية الأجيال',
        'enter': 'اضغط Enter للمتابعة',
        'gen': 'الجيل:',
        'choice_lang': 'اختر لغة مدعومة:',
        'example_lang': 'مثال: أدخل "ar" للعربية'
    },

    ## Korean
    'ko': {
        'commands': '명령어:',
        'enter_button': '명령어 입력:',
        'change_lang': '언어 변경',
        'wid_hei_bx': '[너비] [높이] - 박스 크기 변경',
        'num_of_gen': '[숫자] - 생성 횟수',
        'start': '세포 자동장치 시작',
        'end': '생성 종료',
        'enter': '계속하려면 Enter',
        'gen': '세대:',
        'choice_lang': '지원 언어 선택:',
        'example_lang': '예: "ko" 입력 - 한국어 인터페이스'
    },

    ## Hindi
    'hi': {
        'commands': 'कमांड:',
        'enter_button': 'कमांड दर्ज करें:',
        'change_lang': 'भाषा बदलें',
        'wid_hei_bx': '[चौड़ाई] [ऊंचाई] - बॉक्स आकार बदलें',
        'num_of_gen': '[संख्या] - पीढ़ियों की संख्या',
        'start': 'सेल ऑटोमेटन शुरू करें',
        'end': 'पीढ़ियों का अंत',
        'enter': 'जारी रखने के लिए Enter',
        'gen': 'पीढ़ी:',
        'choice_lang': 'समर्थित भाषा चुनें:',
        'example_lang': 'उदाहरण: "hi" दर्ज करें'
    },

    ## Bengali 
    'bn': {
        'commands': 'কমান্ড:',
        'enter_button': 'কমান্ড ইনপুট:',
        'change_lang': 'ভাষা পরিবর্তন',
        'wid_hei_bx': '[প্রস্থ] [উচ্চতা] - বক্সের আকার পরিবর্তন',
        'num_of_gen': '[সংখ্যা] - প্রজন্ম সংখ্যা',
        'start': 'সেল অটোমেটন শুরু করুন',
        'end': 'প্রজন্মের সমাপ্তি',
        'enter': 'চালিয়ে যেতে Enter',
        'gen': 'প্রজন্ম:',
        'choice_lang': 'সমর্থিত ভাষা নির্বাচন:',
        'example_lang': 'উদাহরণ: "bn" ইনপুট করুন'
    },

    ## Vietnamese
    'vi': {
        'commands': 'Lệnh:',
        'enter_button': 'Nhập lệnh:',
        'change_lang': 'Đổi ngôn ngữ',
        'wid_hei_bx': '[rộng] [cao] - Thay đổi kích thước',
        'num_of_gen': '[số] - Số thế hệ',
        'start': 'Khởi động Automaton tế bào',
        'end': 'Kết thúc thế hệ',
        'enter': 'Nhấn Enter để tiếp tục',
        'gen': 'Thế hệ:',
        'choice_lang': 'Chọn ngôn ngữ hỗ trợ:',
        'example_lang': 'Ví dụ: nhập "vi" cho tiếng Việt'
    },

    ## Chinese Simplified 
    'zh': {
        'commands': '命令:',
        'enter_button': '输入命令:',
        'change_lang': '更改语言',
        'wid_hei_bx': '[宽度] [高度] - 更改区域大小',
        'num_of_gen': '[数字] - 生成代数',
        'start': '启动细胞自动机',
        'end': '生成结束',
        'enter': '按Enter键继续',
        'gen': '世代:',
        'choice_lang': '选择支持的语言:',
        'example_lang': '例如: 输入 "zh" 使用中文'
    },

    ## Japanese
    'ja': {
        'commands': 'コマンド:',
        'enter_button': 'コマンドを入力:',
        'change_lang': '言語を変更',
        'wid_hei_bx': '[幅] [高さ] - 領域サイズを変更',
        'num_of_gen': '[数] - 生成回数',
        'start': 'セルオートマトンを開始',
        'end': '生成終了',
        'enter': 'Enterを押して続行',
        'gen': '世代:',
        'choice_lang': 'サポート言語を選択:',
        'example_lang': '例: "ja" と入力 - 日本語インターフェース'
    },

    ## Javanese 
    'jv': {
        'commands': 'Parentah:',
        'enter_button': 'Input parentah:',
        'change_lang': 'Ganti basa',
        'wid_hei_bx': '[ambane] [dhuwure] - Ganti ukuran kothak',
        'num_of_gen': '[angka] - Pira generasi',
        'start': 'Mulai Automaton Sel',
        'end': 'Pungkasan generasi',
        'enter': 'Pencet Enter kanggo nerusake',
        'gen': 'Generasi:',
        'choice_lang': 'Pilih basa sing didukung:',
        'example_lang': 'Conto: input "jv" - basa Jawa'
    }
}