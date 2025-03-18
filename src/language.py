## You can edit & add new translations!
## 56 language supported!
## Translations may contain errors...

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
[sr] - Српски
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
[ja] - 日本語
[sah] - Саха тыла
[gd] - Gàidhlig (Scottish Gaelic)
[ga] - Gaeilge (Irish)
[cy] - Cymraeg (Welsh)
[br] - Brezhoneg
[hy] - Հայերեն
[ab] - Аҧсуа
[az] - Azərbaycanca
[bua] - Буряад хэлэн
[tyv] - Тыва дыл
[ne] - नेपाली
[sw] - Kiswahili
[ca] - Català 
[eu] - Euskara
[is] - Íslenska 
[ta] - தமிழ் 
[th] - ไทย 
[id] - Bahasa Indonesia 
[ur] - اُردُو 
[zu] - isiZulu 
[ku] - Kurdî 
[lo] - ລາວ """

translations = {
    ## English
    'en': {
        'commands': 'Commands:',
        'enter_button': 'Input your command:',
        'change_lang': 'Change language',
        'wid_hei_bx': '[width] [height] - Change box size',
        'num_of_gen': '[number] - Number of generations',
        'start': '- Start Cell Automaton',
        'end': 'End of generations',
        'enter': 'Press Enter to continue',
        'gen': 'Generation:',
        'choice_lang': 'Select supported language:',
        'example_lang': 'Example: input "en" for English',
        'seed':'[seed] - generating seed',
    },

    ## Russian
    'ru': {
        'commands': 'Команды:',
        'enter_button': 'Введите команду:',
        'change_lang': 'Сменить язык',
        'wid_hei_bx': '[ширина] [высота] - Изменить размер области',
        'num_of_gen': '[число] - Количество поколений',
        'start': '- Запустить клеточный автомат',
        'end': 'Конец генераций',
        'enter': 'Нажмите Enter для продолжения',
        'gen': 'Поколение:',
        'choice_lang': 'Выберите язык:',
        'example_lang': 'Пример: введите "ru" для русского',
        'seed': '[seed] - сид для генерации'
    },

    ## Spanish
    'es': {
        'commands': 'Comandos:',
        'enter_button': 'Ingrese comando:',
        'change_lang': 'Cambiar idioma',
        'wid_hei_bx': '[ancho] [alto] - Cambiar tamaño',
        'num_of_gen': '[número] - Número de generaciones',
        'start': '- Iniciar autómata celular',
        'end': 'Fin de generaciones',
        'enter': 'Presione Enter para continuar',
        'gen': 'Generación:',
        'choice_lang': 'Seleccione idioma:',
        'example_lang': 'Ejemplo: ingrese "es" para español',
        'seed':'[seed] - semilla generadora',
    },

    ## French
    'fr': {
        'commands': 'Commandes:',
        'enter_button': 'Saisir commande:',
        'change_lang': 'Changer de langue',
        'wid_hei_bx': '[largeur] [hauteur] - Modifier taille',
        'num_of_gen': '[nombre] - Nombre de générations',
        'start': '- Démarrer automate cellulaire',
        'end': 'Fin des générations',
        'enter': 'Appuyez sur Entrée',
        'gen': 'Génération:',
        'choice_lang': 'Choisir langue:',
        'example_lang': 'Exemple: "fr" pour français',
        'seed':'[seed] - graine génératrice',
    },

    ## German
    'de': {
        'commands': 'Befehle:',
        'enter_button': 'Befehl eingeben:',
        'change_lang': 'Sprache ändern',
        'wid_hei_bx': '[Breite] [Höhe] - Größe ändern',
        'num_of_gen': '[Anzahl] - Generationen',
        'start': '- Zellularautomat starten',
        'end': 'Ende der Generationen',
        'enter': 'Enter drücken',
        'gen': 'Generation:',
        'choice_lang': 'Sprache wählen:',
        'example_lang': 'Beispiel: "de" für Deutsch',
        'seed':'[seed] - Generierungs-Seed',
    },

    ## Dutch
    'nl': {
        'commands': 'Commando\'s:',
        'enter_button': 'Voer opdracht in:',
        'change_lang': 'Taal wijzigen',
        'wid_hei_bx': '[breedte] [hoogte] - Grootte wijzigen',
        'num_of_gen': '[aantal] - Aantal generaties',
        'start': '- Start cellulaire automaat',
        'end': 'Einde generaties',
        'enter': 'Druk op Enter',
        'gen': 'Generatie:',
        'choice_lang': 'Selecteer taal:',
        'example_lang': 'Voorbeeld: "nl" voor Nederlands',
        'seed':'[seed] - genererende seed',     
    },

    ## Italian
    'it': {
        'commands': 'Comandi:',
        'enter_button': 'Inserisci comando:',
        'change_lang': 'Cambia lingua',
        'wid_hei_bx': '[larghezza] [altezza] - Modifica dimensione',
        'num_of_gen': '[numero] - Numero di generazioni',
        'start': '- Avvia automa cellulare',
        'end': 'Fine generazioni',
        'enter': 'Premi Invio',
        'gen': 'Generazione:',
        'choice_lang': 'Seleziona lingua:',
        'example_lang': 'Esempio: "it" per italiano',
        'seed':'[seed] - seme generativo',
    },

    ## Swedish
    'sv': {
        'commands': 'Kommandon:',
        'enter_button': 'Ange kommando:',
        'change_lang': 'Ändra språk',
        'wid_hei_bx': '[bredd] [höjd] - Ändra storlek',
        'num_of_gen': '[antal] - Antal generationer',
        'start': '- Starta cellautomat',
        'end': 'Slut på generationer',
        'enter': 'Tryck Enter',
        'gen': 'Generation:',
        'choice_lang': 'Välj språk:',
        'example_lang': 'Exempel: "sv" för svenska',
        'seed':'[seed] - genererande frö',
    },

    ## Danish
    'da': {
        'commands': 'Kommandoer:',
        'enter_button': 'Indtast kommando:',
        'change_lang': 'Skift sprog',
        'wid_hei_bx': '[bredde] [højde] - Ændr størrelse',
        'num_of_gen': '[antal] - Antal generationer',
        'start': '- Start celleautomat',
        'end': 'Slut på generationer',
        'enter': 'Tryk Enter',
        'gen': 'Generation:',
        'choice_lang': 'Vælg sprog:',
        'example_lang': 'Eksempel: "da" for dansk',
        'seed':'[seed] - genererende frø',
    },

    ## Norwegian
    'no': {
        'commands': 'Kommandoer:',
        'enter_button': 'Skriv inn kommando:',
        'change_lang': 'Bytt språk',
        'wid_hei_bx': '[bredde] [høyde] - Endre størrelse',
        'num_of_gen': '[antall] - Antall generasjoner',
        'start': '- Start celleautomat',
        'end': 'Slutt på generasjoner',
        'enter': 'Trykk Enter',
        'gen': 'Generasjon:',
        'choice_lang': 'Velg språk:',
        'example_lang': 'Eksempel: "no" for norsk',
        'seed':'[seed] - ziarno generujące',
    },

    ## Polish
    'pl': {
        'commands': 'Polecenia:',
        'enter_button': 'Wprowadź polecenie:',
        'change_lang': 'Zmień język',
        'wid_hei_bx': '[szerokość] [wysokość] - Zmień rozmiar',
        'num_of_gen': '[liczba] - Liczba generacji',
        'start': '- Uruchom automat komórkowy',
        'end': 'Koniec generacji',
        'enter': 'Naciśnij Enter',
        'gen': 'Generacja:',
        'choice_lang': 'Wybierz język:',
        'example_lang': 'Przykład: "pl" dla polskiego',
        'seed':'[seed] - generující semeno',
    },

    ## Czech
    'cs': {
        'commands': 'Příkazy:',
        'enter_button': 'Zadejte příkaz:',
        'change_lang': 'Změnit jazyk',
        'wid_hei_bx': '[šířka] [výška] - Změnit velikost',
        'num_of_gen': '[číslo] - Počet generací',
        'start': '- Spustit buněčný automat',
        'end': 'Konec generací',
        'enter': 'Stiskněte Enter',
        'gen': 'Generace:',
        'choice_lang': 'Vyberte jazyk:',
        'example_lang': 'Příklad: "cs" pro češtinu',

    },

    ## Slovak
    'sk': {
        'commands': 'Príkazy:',
        'enter_button': 'Zadajte príkaz:',
        'change_lang': 'Zmeniť jazyk',
        'wid_hei_bx': '[šírka] [výška] - Zmeniť veľkosť oblasti',
        'num_of_gen': '[číslo] - Počet generácií',
        'start': '- Spustiť bunkový automat',
        'end': 'Koniec generácií',
        'enter': 'Stlačte Enter pre pokračovanie',
        'gen': 'Generácia:',
        'choice_lang': 'Vyberte podporovaný jazyk zo zoznamu:',
        'example_lang': 'Príklad: zadajte "sk" pre slovenské rozhranie',
        'seed':'[seed] - generujúce semeno',
    },

    ## Serbian - Cyrillic
    'sr': {
        'commands': 'Команде:',
        'enter_button': 'Унесите команду:',
        'change_lang': 'Промени језик',
        'wid_hei_bx': '[ширина] [висина] - Промени величину',
        'num_of_gen': '[број] - Број генерација',
        'start': '- Покрени ћелијски аутомат',
        'end': 'Крај генерација',
        'enter': 'Притисните Enter за наставак',
        'gen': 'Генерација:',
        'choice_lang': 'Изаберите језик са списка:',
        'example_lang': 'Пример: унесите "sr" за српски интерфејс',
        'seed':'[seed] - генераторско семе',
    },

    ## Bulgarian 
    'bg': {
        'commands': 'Команди:',
        'enter_button': 'Въведете команда:',
        'change_lang': 'Смени език',
        'wid_hei_bx': '[широчина] [височина] - Промяна на размера',
        'num_of_gen': '[число] - Брой поколения',
        'start': '- Стартирай клетъчен автомат',
        'end': 'Край на поколенията',
        'enter': 'Натиснете Enter',
        'gen': 'Поколение:',
        'choice_lang': 'Изберете език от списъка:',
        'example_lang': 'Пример: въведете "bg" за български интерфейс',
        'seed':'[seed] - генериращо семе',
    },

    ## Hungarian
    'hu': {
        'commands': 'Parancsok:',
        'enter_button': 'Parancs bevitele:',
        'change_lang': 'Nyelv váltása',
        'wid_hei_bx': '[szélesség] [magasság] - Méret változtatása',
        'num_of_gen': '[szám] - Generációk száma',
        'start': '- Cellularis automata indítása',
        'end': 'Generációk vége',
        'enter': 'Nyomja meg az Entert',
        'gen': 'Generáció:',
        'choice_lang': 'Válasszon nyelvet a listából:',
        'example_lang': 'Például: írja be "hu" magyar nyelvhez',
        'seed':'[seed] - generáló mag',
    },

    ## Greek 
    'el': {
        'commands': 'Εντολές:',
        'enter_button': 'Εισαγωγή εντολής:',
        'change_lang': 'Αλλαγή γλώσσας',
        'wid_hei_bx': '[πλάτος] [ύψος] - Αλλαγή μεγέθους',
        'num_of_gen': '[αριθμός] - Αριθμός γενεών',
        'start': '- Εκκίνηση κυτταρικού αυτόματου',
        'end': 'Τέλος γενεών',
        'enter': 'Πατήστε Enter',
        'gen': 'Γενιά:',
        'choice_lang': 'Επιλέξτε γλώσσα από τη λίστα:',
        'example_lang': 'Παράδειγμα: εισάγετε "el" για ελληνική διεπαφή',
        'seed':'[seed] - σπόρος παραγωγής',
    },

    ## Finnish
    'fi': {
        'commands': 'Komennot:',
        'enter_button': 'Syötä komento:',
        'change_lang': 'Vaihda kieltä',
        'wid_hei_bx': '[leveys] [korkeus] - Muuta laatikon kokoa',
        'num_of_gen': '[määrä] - Sukupolvien määrä',
        'start': '- Käynnistä soluautomaatti',
        'end': 'Sukupolvien loppu',
        'enter': 'Paina Enter jatkaaksesi',
        'gen': 'Sukupolvi:',
        'choice_lang': 'Valitse tuettu kieli listasta:',
        'example_lang': 'Esimerkiksi: syötä "fi" suomen kielelle',
        'seed':'[seed] - generoiva siemen',
    },

    ## Turkish 
    'tr': {
        'commands': 'Komutlar:',
        'enter_button': 'Komut girin:',
        'change_lang': 'Dili değiştir',
        'wid_hei_bx': '[genişlik] [yükseklik] - Kutu boyutunu değiştir',
        'num_of_gen': '[sayı] - Nesil sayısı',
        'start': '- Hücresel Otomat Başlat',
        'end': 'Nesil sonu',
        'enter': 'Devam etmek için Enter\'a basın',
        'gen': 'Nesil:',
        'choice_lang': 'Listeden desteklenen bir dil seçin:',
        'example_lang': 'Örneğin: "tr" yazın - Türkçe arayüz için',
        'seed':'[seed] - oluşturucu tohum',
    },

    ## Portuguese 
    'pt': {
        'commands': 'Comandos:',
        'enter_button': 'Insira seu comando:',
        'change_lang': 'Mudar idioma',
        'wid_hei_bx': '[largura] [altura] - Alterar tamanho da caixa',
        'num_of_gen': '[número] - Número de gerações',
        'start': '- Iniciar Autômato Celular',
        'end': 'Fim das gerações',
        'enter': 'Pressione Enter para continuar',
        'gen': 'Geração:',
        'choice_lang': 'Selecione um idioma da lista:',
        'example_lang': 'Exemplo: digite "pt" para português',
        'seed':'[seed] - semente geradora',
    },

    ## Albanian
    'sq': {
        'commands': 'Komandat:',
        'enter_button': 'Shkruaj komandën:',
        'change_lang': 'Ndrysho gjuhën',
        'wid_hei_bx': '[gjerësia] [lartësia] - Ndrysho madhësinë e kutisë',
        'num_of_gen': '[numri] - Numri i gjeneratave',
        'start': '- Nis Automatin Qelizor',
        'end': 'Fundi i gjeneratave',
        'enter': 'Shtyp Enter për të vazhduar',
        'gen': 'Gjenerata:',
        'choice_lang': 'Zgjidhni një gjuhë nga lista:',
        'example_lang': 'P.sh.: shkruani "sq" për shqip',
        'seed':'[seed] - farë gjeneruese',
    },

    ## Georgian 
    'ka': {
        'commands': 'ბრძანებები:',
        'enter_button': 'შეიყვანეთ ბრძანება:',
        'change_lang': 'ენის შეცვლა',
        'wid_hei_bx': '[სიგანე] [სიმაღლე] - ყუთის ზომის შეცვლა',
        'num_of_gen': '[რიცხვი] - თაობების რაოდენობა',
        'start': '- უჯრედოვანი ავტომატის გაშვება',
        'end': 'თაობების დასასრული',
        'enter': 'გასაგრძელებლად დააჭირეთ Enter-ს',
        'gen': 'თაობა:',
        'choice_lang': 'აირჩიეთ ენა სიიდან:',
        'example_lang': 'მაგალითად: შეიყვანეთ "ka" ქართული ინტერფეისისთვის',
        'seed':'[seed] - მომტვინები თესლი',
    },

    ## Esperanto 
    'eo': {
        'commands': 'Komandoj:',
        'enter_button': 'Enigu vian komon:',
        'change_lang': 'Ŝanĝi lingvon',
        'wid_hei_bx': '[larĝo] [alto] - Ŝanĝi skatolan grandecon',
        'num_of_gen': '[nombro] - Nombro de generacioj',
        'start': '- Starti ĉelan aŭtomaton',
        'end': 'Fino de generacioj',
        'enter': 'Premu Enter por daŭrigi',
        'gen': 'Generacio:',
        'choice_lang': 'Elektu subtenatan lingvon:',
        'example_lang': 'Ekzemple: enigu "eo" por Esperanto',
        'seed':'[seed] - generanta semo',
    },

    ## Persian/Farsi 
    'fa': {
        'commands': 'دستورات:',
        'enter_button': 'دستور خود را وارد کنید:',
        'change_lang': 'تغییر زبان',
        'wid_hei_bx': '[عرض] [ارتفاع] - تغییر اندازه جعبه',
        'num_of_gen': '[عدد] - تعداد نسل‌ها',
        'start': '- شروع اتومات سلولی',
        'end': 'پایان نسل‌ها',
        'enter': 'ادامه با Enter',
        'gen': 'نسل:',
        'choice_lang': 'زبان پشتیبانی شده انتخاب کنید:',
        'example_lang': 'مثال: "fa" را برای فارسی وارد کنید',
        'seed':'[seed] - بذر مولد',
    },

    ## Uzbek
    'uz': {
        'commands': 'Buyruqlar:',
        'enter_button': 'Buyruq kiriting:',
        'change_lang': 'Tilni o\'zgartirish',
        'wid_hei_bx': '[eni] [balandligi] - Quti o\'lchamini o\'zgartirish',
        'num_of_gen': '[son] - Necha avlod',
        'start': '- Hujayrali avtomatni boshlash',
        'end': 'Avlodlar tugadi',
        'enter': 'Davom etish uchun Enter',
        'gen': 'Avlod:',
        'choice_lang': 'Ro\'yxatdan tilni tanlang:',
        'example_lang': 'Masalan: "uz" kiriting',
        'seed':'[seed] - generatsiya qiluvchi urugʻ',
    },

    ## Mongolian - Cyrillic
    'mn': {
        'commands': 'Командууд:',
        'enter_button': 'Командаа оруулна уу:',
        'change_lang': 'Хэл солих',
        'wid_hei_bx': '[өргөн] [өндөр] - Хайрцгийн хэмжээ солих',
        'num_of_gen': '[тоо] - Үеийн тоо',
        'start': '- Эсний автомат эхлүүлэх',
        'end': 'Үеийн төгсгөл',
        'enter': 'Үргэлжлүүлэх Enter',
        'gen': 'Үе:',
        'choice_lang': 'Дэмжигдсэн хэлийг сонгоно уу:',
        'example_lang': 'Жишээ нь: "mn" оруулна уу',
        'seed':'[seed] - үүсгэх үр',
    },

    ## Hebrew - RTL
    'he': {
        'commands': 'פקודות:',
        'enter_button': 'הזן פקודה:',
        'change_lang': 'שנה שפה',
        'wid_hei_bx': '[רוחב] [גובה] - שנה גודל תיבה',
        'num_of_gen': '[מספר] - מספר דורות',
        'start': '- התחל אוטומט תאים',
        'end': 'סוף הדורות',
        'enter': 'הקש Enter להמשך',
        'gen': 'דור:',
        'choice_lang': 'בחר שפה נתמכת:',
        'example_lang': 'לדוגמה: הקש "he" לעברית',
        'seed':'[seed] - זרע מייצר',
    },

    ## Arabic - RTL
    'ar': {
        'commands': 'الأوامر:',
        'enter_button': 'أدخل الأمر:',
        'change_lang': 'تغيير اللغة',
        'wid_hei_bx': '[العرض] [الارتفاع] - تغيير حجم الصندوق',
        'num_of_gen': '[العدد] - عدد الأجيال',
        'start': '- بدء الأوتومات الخلوي',
        'end': 'نهاية الأجيال',
        'enter': 'اضغط Enter للمتابعة',
        'gen': 'الجيل:',
        'choice_lang': 'اختر لغة مدعومة:',
        'example_lang': 'مثال: أدخل "ar" للعربية',
        'seed':'[seed] - بذرة توليد',
    },

    ## Korean
    'ko': {
        'commands': '명령어:',
        'enter_button': '명령어 입력:',
        'change_lang': '언어 변경',
        'wid_hei_bx': '[너비] [높이] - 박스 크기 변경',
        'num_of_gen': '[숫자] - 생성 횟수',
        'start': '- 세포 자동장치 시작',
        'end': '생성 종료',
        'enter': '계속하려면 Enter',
        'gen': '세대:',
        'choice_lang': '지원 언어 선택:',
        'example_lang': '예: "ko" 입력 - 한국어 인터페이스',
        'seed':'[seed] - 생성 시드',
    },

    ## Hindi
    'hi': {
        'commands': 'कमांड:',
        'enter_button': 'कमांड दर्ज करें:',
        'change_lang': 'भाषा बदलें',
        'wid_hei_bx': '[चौड़ाई] [ऊंचाई] - बॉक्स आकार बदलें',
        'num_of_gen': '[संख्या] - पीढ़ियों की संख्या',
        'start': '- सेल ऑटोमेटन शुरू करें',
        'end': 'पीढ़ियों का अंत',
        'enter': 'जारी रखने के लिए Enter',
        'gen': 'पीढ़ी:',
        'choice_lang': 'समर्थित भाषा चुनें:',
        'example_lang': 'उदाहरण: "hi" दर्ज करें',
        'seed':'[seed] - उत्पन्न करने वाला बीज',
    },

    ## Bengali 
    'bn': {
        'commands': 'কমান্ড:',
        'enter_button': 'কমান্ড ইনপুট:',
        'change_lang': 'ভাষা পরিবর্তন',
        'wid_hei_bx': '[প্রস্থ] [উচ্চতা] - বক্সের আকার পরিবর্তন',
        'num_of_gen': '[সংখ্যা] - প্রজন্ম সংখ্যা',
        'start': '- সেল অটোমেটন শুরু করুন',
        'end': 'প্রজন্মের সমাপ্তি',
        'enter': 'চালিয়ে যেতে Enter',
        'gen': 'প্রজন্ম:',
        'choice_lang': 'সমর্থিত ভাষা নির্বাচন:',
        'example_lang': 'উদাহরণ: "bn" ইনপুট করুন',
        'seed':'[seed] - জেনারেটিং বীজ',
    },

    ## Vietnamese
    'vi': {
        'commands': 'Lệnh:',
        'enter_button': 'Nhập lệnh:',
        'change_lang': 'Đổi ngôn ngữ',
        'wid_hei_bx': '[rộng] [cao] - Thay đổi kích thước',
        'num_of_gen': '[số] - Số thế hệ',
        'start': '- Khởi động Automaton tế bào',
        'end': 'Kết thúc thế hệ',
        'enter': 'Nhấn Enter để tiếp tục',
        'gen': 'Thế hệ:',
        'choice_lang': 'Chọn ngôn ngữ hỗ trợ:',
        'example_lang': 'Ví dụ: nhập "vi" cho tiếng Việt',
        'seed':'[seed] - hạt giống tạo ra',
    },

    ## Chinese Simplified 
    'zh': {
        'commands': '命令:',
        'enter_button': '输入命令:',
        'change_lang': '更改语言',
        'wid_hei_bx': '[宽度] [高度] - 更改区域大小',
        'num_of_gen': '[数字] - 生成代数',
        'start': '- 启动细胞自动机',
        'end': '生成结束',
        'enter': '按Enter键继续',
        'gen': '世代:',
        'choice_lang': '选择支持的语言:',
        'example_lang': '例如: 输入 "zh" 使用中文',
        'seed':'[seed] - 生成种子',
    },

    ## Japanese
    'ja': {
        'commands': 'コマンド:',
        'enter_button': 'コマンドを入力:',
        'change_lang': '言語を変更',
        'wid_hei_bx': '[幅] [高さ] - 領域サイズを変更',
        'num_of_gen': '[数] - 生成回数',
        'start': '- セルオートマトンを開始',
        'end': '生成終了',
        'enter': 'Enterを押して続行',
        'gen': '世代:',
        'choice_lang': 'サポート言語を選択:',
        'example_lang': '例: "ja" と入力 - 日本語インターフェース',
        'seed':'[seed] - 生成シード',
    },

    ## Javanese 
    'jv': {
        'commands': 'Parentah:',
        'enter_button': 'Input parentah:',
        'change_lang': 'Ganti basa',
        'wid_hei_bx': '[ambane] [dhuwure] - Ganti ukuran kothak',
        'num_of_gen': '[angka] - Pira generasi',
        'start': '- Mulai Automaton Sel',
        'end': 'Pungkasan generasi',
        'enter': 'Pencet Enter kanggo nerusake',
        'gen': 'Generasi:',
        'choice_lang': 'Pilih basa sing didukung:',
        'example_lang': 'Conto: input "jv" - basa Jawa',
        'seed': 'Generasi wiji',
    },

    ## Yakutian 
    'sah':  {
    'commands': 'Командалар:',
    'enter_button': 'Командаҕыты киллэриҥ:',
    'change_lang': 'Тыл уларытыы',
    'wid_hei_bx': '[width] [height] - Боксу кээмэйин уларытыы',
    'num_of_gen': '[number] - Поколениелар ахсааннара',
    'start': '- Клетка автоматонун саҕалыырга',
    'end': 'Поколениелар бүтүүлэрэ',
    'enter': 'Салгыырга Enter баттаа',
    'gen': 'Поколение:',
    'choice_lang': 'Тилин таллар:',
    'example_lang': 'Холобур: Ааҥыл тылыгар "en" киллэр',
    'seed': '[оҥоруу] - Төрүтү оҥоруу',
    },

    ## Buryat
    'bua': {
        'commands': 'Командууд:',
        'enter_button': 'Командаа оруулна уу:',
        'change_lang': 'Хэл солих',
        'wid_hei_bx': '[өргөн] [өндөр] - Хайрцганы хэмжээ солих',
        'num_of_gen': '[тоо] - Үеийн тоо',
        'start': '- Эс Автоматон эхлүүлэх',
        'end': 'Үеийн төгсгөл',
        'enter': 'Үргэлжлүүлэхэд Enter дараарай',
        'gen': 'Үе:',
        'choice_lang': 'Дэмжигдсэн хэлийг сонгоно уу:',
        'example_lang': 'Жишээ: англи хэлдээ "en" оруулна уу',
        'seed': '[үр] - үр үүсгэх',
    },

    ## Tuvan
    'tyv': {
        'commands': 'Командалар:',
        'enter_button': 'Командаңызы киириңер:',
        'change_lang': 'Дыл солуур',
        'wid_hei_bx': '[албада] [бедик] - Кутузуң хемчээлин солуур',
        'num_of_gen': '[саны] - Өскүлерниң саны',
        'start': '- Хөрең Автоматон эгелээр',
        'end': 'Өскүлерниң төнчүзү',
        'enter': 'Уламчылаарга Enter базыңар',
        'gen': 'Өскү:',
        'choice_lang': 'Дөзүрелген дылды таңзыңар:',
        'example_lang': 'Херекчү: англи дылда "en" киириңер',
        'seed': '[үре] - үре кылыр',
    },

    ## Scottish Gaelic
    'gd': { 
        'commands': 'Òrdughan:',
        'enter_button': 'Cuir a-steach do àithne:',
        'change_lang': 'Athraich an cànan',
        'wid_hei_bx': '[leud] [àirde] - Atharraich meud a’ bhogsa',
        'num_of_gen': '[àireamh] - Àireamh nan ginealach',
        'start': '- Tòisich Automaton Cealla',
        'end': 'Deireadh nan ginealach',
        'enter': 'Brùth Enter airson leantainn',
        'gen': 'Ginealach:',
        'choice_lang': 'Tagh cànan taiceil:',
        'example_lang': 'Eisimpleir: cuir a-steach "en" airson Beurla',
        'seed': '[sìol] - a’ gineadh sìol',
    },

    ## Irish
    'ga': { 
        'commands': 'Orduithe:',
        'enter_button': 'Iontráil d’ordú:',
        'change_lang': 'Athraigh teanga',
        'wid_hei_bx': '[leithead] [airde] - Athraigh méid an bhosca',
        'num_of_gen': '[uimhir] - Líon na nglúin',
        'start': '- Tosaigh Uathóglú Cille',
        'end': 'Deireadh na nglúin',
        'enter': 'Brúigh Enter chun leanúint ar aghaidh',
        'gen': 'Glúin:',
        'choice_lang': 'Roghnaigh teanga a dtacaítear léi:',
        'example_lang': 'Sampla: cuir isteach "en" le haghaidh Béarla',
        'seed': '[síol] - síol a ghiniúint',
    },

    ## Welsh
    'cy': { 
        'commands': 'Gorchmynion:',
        'enter_button': 'Rhowch eich gorchymyn:',
        'change_lang': 'Newid iaith',
        'wid_hei_bx': '[lled] [uchder] - Newid maint y blwch',
        'num_of_gen': '[rhif] - Nifer y cenhedloedd',
        'start': '- Dechrau Awtofediannau Cell',
        'end': 'Diwedd y cenhedloedd',
        'enter': 'Pwyswch Enter i barhau',
        'gen': 'Cenhedlaeth:',
        'choice_lang': 'Dewiswch iaith a gynhelir:',
        'example_lang': 'Enghraifft: rhowch "en" am Saesneg',
        'seed': '[had] - cynhyrchu had',
    },

    ## Breton
    'br': { 
        'commands': 'Arc\'hadoù:',
        'enter_button': 'Roit ho urzh:',
        'change_lang': 'Kemm yezh',
        'wid_hei_bx': '[led] [uhelder] - Kemm ment ar voest',
        'num_of_gen': '[niver] - Niver a remziadoù',
        'start': '- Kregiñ ar C\'hell Awtomat',
        'end': 'Fin ar remziadoù',
        'enter': 'Pouezañ war Enter evit kenderc\'hel',
        'gen': 'Remziad:',
        'choice_lang': 'Dibabit ur yezh skoret:',
        'example_lang': 'Skouer: enankit "en" evit saozneg',
        'seed': '[had] - genel had',
    },

    ## Armenian
    'hy': {
        'commands': 'Հրամաններ:',
        'enter_button': 'Մուտքագրեք ձեր հրամանը:',
        'change_lang': 'Փոխել լեզուն',
        'wid_hei_bx': '[լայնություն] [բարձրություն] - Փոխել տուփի չափը',
        'num_of_gen': '[թիվ] - Սերունդների քանակը',
        'start': '- Սկսել բջջային ավտոմատ',
        'end': 'Սերունդների ավարտը',
        'enter': 'Շարունակելու համար սեղմեք Enter',
        'gen': 'Սերունդ:',
        'choice_lang': 'Ընտրեք աջակցվող լեզուն:',
        'example_lang': 'Օրինակ՝ մուտքագրեք "en" անգլերենի համար',
        'seed': '[սերմ] - սերմի ստեղծում',
    },

    ## Abkhaz
    'ab': { 
        'commands': 'Акомандақәа:',
        'enter_button': 'Урҭ акомандақәа рзы:',
        'change_lang': 'Абызшәа аҧыхра',
        'wid_hei_bx': '[аҧҵа] [аҩаша] - Аҧыла абара шәаҧхьаӡара',
        'num_of_gen': '[аҩбатәи] - Арбарақәа рхыԥхьаӡара',
        'start': '- Аҧылаҿтәи аутоматон аԥхьаӡа',
        'end': 'Арбарақәа рҽаԥхьа',
        'enter': 'Иаԥҵареи Enter ҳасуп',
        'gen': 'Арбара:',
        'choice_lang': 'Иаҳарауақәа рзы абызшәақәа рыҧхьаӡа:',
        'example_lang': 'Амисаҭқәа: "en" англыз бызшәа рзы',
        'seed': '[аҧсад] - аҧсад аҧҵаразы',
    },

    ## Azerbaijani
    'az': {
        'commands': 'Əmrlər:',
        'enter_button': 'Əmrinizi daxil edin:',
        'change_lang': 'Dili dəyiş',
        'wid_hei_bx': '[eni] [hündürlük] - Qutu ölçüsünü dəyişdir',
        'num_of_gen': '[sayı] - Nəsillərin sayı',
        'start': '- Hücri Avtomatı Başlat',
        'end': 'Nəsillərin sonu',
        'enter': 'Davam etmək üçün Enter düyməsini basın',
        'gen': 'Nəsil:',
        'choice_lang': 'Dəstəklənən dili seçin:',
        'example_lang': 'Məsələn: ingiliscə üçün "en" daxil edin',
        'seed': '[toxum] - toxum yaratmaq',
    },

    ## Nepali (Devanagari)
    'ne': {
        'commands': 'आदेशहरू:',
        'enter_button': 'आफ्नो आदेश प्रविष्ट गर्नुहोस्:',
        'change_lang': 'भाषा परिवर्तन गर्नुहोस्',
        'wid_hei_bx': '[चौडाइ] [उचाइ] - बक्सको आकार परिवर्तन गर्नुहोस्',
        'num_of_gen': '[संख्या] - पुस्ताहरूको संख्या',
        'start': '- सेल स्वचालित सुरु गर्नुहोस्',
        'end': 'पुस्ताहरूको अन्त्य',
        'enter': 'जारी राख्न Enter थिच्नुहोस्',
        'gen': 'पुस्ता:',
        'choice_lang': 'समर्थित भाषा चयन गर्नुहोस्:',
        'example_lang': 'उदाहरण: अङ्ग्रेजीको लागि "en" प्रविष्ट गर्नुहोस्',
        'seed': 'बीउ - बीउ सिर्जना गर्दै',
    },

    ## Swahili
    'sw': {
        'commands': 'Amri:',
        'enter_button': 'Weka amri yako:',
        'change_lang': 'Badilisha lugha',
        'wid_hei_bx': '[upana] [urefu] - Badilisha ukubwa wa boksi',
        'num_of_gen': '[nambari] - Idadi ya vizazi',
        'start': '- Anza Otomati ya Selu',
        'end': 'Mwisho wa vizazi',
        'enter': 'Bonyeza Enter kuendelea',
        'gen': 'Kizazi:',
        'choice_lang': 'Chagua lugha inayoungwa mkono:',
        'example_lang': 'Mfano: weka "en" kwa Kiingereza',
        'seed': '[mbegu] - kutengeneza mbegu',
    },

    ## Catalan
    'ca': { 
        'commands': 'Comandes:',
        'enter_button': 'Introdueix la teva comanda:',
        'change_lang': 'Canvia l\'idioma',
        'wid_hei_bx': '[amplada] [alçada] - Canvia la mida de la caixa',
        'num_of_gen': '[nombre] - Nombre de generacions',
        'start': '- Iniciar l\'Automata Cel·lular',
        'end': 'Fi de les generacions',
        'enter': 'Prem Enter per continuar',
        'gen': 'Generació:',
        'choice_lang': 'Selecciona un idioma suportat:',
        'example_lang': 'Exemple: introdueix "en" per anglès',
        'seed': '[llavor] - generació de llavor',
    },

    ## Basque
    'eu': {
        'commands': 'Komandoak:',
        'enter_button': 'Sartu zure komandoa:',
        'change_lang': 'Hizkuntza aldatu',
        'wid_hei_bx': '[zabalera] [altuera] - Kutxaren tamaina aldatu',
        'num_of_gen': '[zenbakia] - Belaunaldi kopurua',
        'start': '- Zelula Automatoa abiarazi',
        'end': 'Belaunaldien amaiera',
        'enter': 'Sakatu Enter jarraitzeko',
        'gen': 'Belaunaldia:',
        'choice_lang': 'Aukeratu onartutako hizkuntza:',
        'example_lang': 'Adibidea: sartu "en" ingelerarako',
        'seed': '[hazi] - hazia sortzen',
    },

    ## Icelandic
    'is': {
        'commands': 'Skipanir:',
        'enter_button': 'Sláðu inn skipun:',
        'change_lang': 'Breyta tungumáli',
        'wid_hei_bx': '[breidd] [hæð] - Breyta stærð kassans',
        'num_of_gen': '[fjöldi] - Fjöldi kynslóða',
        'start': '- Byrjaðu á Frumufjölgun',
        'end': 'Endir kynslóða',
        'enter': 'Ýttu á Enter til að halda áfram',
        'gen': 'Kynslóð:',
        'choice_lang': 'Veldu studd tungumál:',
        'example_lang': 'Dæmi: sláðu inn "en" fyrir ensku',
        'seed': '[fræ] - búa til fræ',
    },

    ## Tamil
    'ta': {
        'commands': 'கட்டளைகள்:',
        'enter_button': 'உங்கள் கட்டளையை உள்ளிடவும்:',
        'change_lang': 'மொழியை மாற்று',
        'wid_hei_bx': '[அகலம்] [உயரம்] - பெட்டியின் அளவை மாற்று',
        'num_of_gen': '[எண்] - தலைமுறைகளின் எண்ணிக்கை',
        'start': '- செல் ஆட்டோமேட்டன் தொடங்கு',
        'end': 'தலைமுறைகளின் முடிவு',
        'enter': 'தொடர Enter அழுத்தவும்',
        'gen': 'தலைமுறை:',
        'choice_lang': 'ஆதரவு உள்ள மொழியைத் தேர்ந்தெடு:',
        'example_lang': 'எடுத்துக்காட்டு: ஆங்கிலத்திற்கு "en" உள்ளிடவும்',
        'seed': '[விதை] - விதை உருவாக்கம்',
    },

    ## Thai
    'th': {
        'commands': 'คำสั่ง:',
        'enter_button': 'ป้อนคำสั่งของคุณ:',
        'change_lang': 'เปลี่ยนภาษา',
        'wid_hei_bx': '[ความกว้าง] [ความสูง] - เปลี่ยนขนาดกล่อง',
        'num_of_gen': '[จำนวน] - จำนวนรุ่น',
        'start': '- เริ่มต้นเซลล์ออโตมาตอน',
        'end': 'สิ้นสุดรุ่น',
        'enter': 'กด Enter เพื่อดำเนินการต่อ',
        'gen': 'รุ่น:',
        'choice_lang': 'เลือกภาษาที่รองรับ:',
        'example_lang': 'ตัวอย่าง: ป้อน "en" สำหรับภาษาอังกฤษ',
        'seed': '[เมล็ด] - การสร้างเมล็ด',
    },

    ## Indonesian
    'id': { 
        'commands': 'Perintah:',
        'enter_button': 'Masukkan perintah Anda:',
        'change_lang': 'Ubah bahasa',
        'wid_hei_bx': '[lebar] [tinggi] - Ubah ukuran kotak',
        'num_of_gen': '[jumlah] - Jumlah generasi',
        'start': '- Mulai Automaton Sel',
        'end': 'Akhir generasi',
        'enter': 'Tekan Enter untuk melanjutkan',
        'gen': 'Generasi:',
        'choice_lang': 'Pilih bahasa yang didukung:',
        'example_lang': 'Contoh: masukkan "en" untuk bahasa Inggris',
        'seed': '[biji] - menghasilkan benih',
    },

    ## Urdu
    'ur': {  
        'commands': 'کمندیں:',
        'enter_button': 'اپنا کمانڈ درج کریں:',
        'change_lang': 'زبان تبدیل کریں',
        'wid_hei_bx': '[چوڑائی] [اونچائی] - باکس کا سائز تبدیل کریں',
        'num_of_gen': '[تعداد] - نسلوں کی تعداد',
        'start': '- سیل آٹومیٹون شروع کریں',
        'end': 'نسلوں کا اختتام',
        'enter': 'جاری رکھنے کے لیے انٹر دبائیں',
        'gen': 'نسل:',
        'choice_lang': 'معاون زبان منتخب کریں:',
        'example_lang': 'مثال: انگریزی کے لیے "en" درج کریں',
        'seed': '[بیج] - بیج پیدا کرنا',
    },
    
    ## Zulu
    'zu': {
        'commands': 'Imiyalo:',
        'enter_button': 'Faka umyalo wakho:',
        'change_lang': 'Shintsha ulimi',
        'wid_hei_bx': '[ububanzi] [ukuphakama] - Shintsha usayizi webhokisi',
        'num_of_gen': '[inombolo] - Inani lezizukulwane',
        'start': '- Qala i-Automaton Yamaseli',
        'end': 'Isiphetho sezizukulwane',
        'enter': 'Cindezela u-Enter ukuze uqhubeke',
        'gen': 'Isizukulwane:',
        'choice_lang': 'Khetha ulimi olusekelwayo:',
        'example_lang': 'Isibonelo: faka "en" ngesiNgisi',
        'seed': '[imbewu] - ukudala imbewu',
    },

    ## Kurdish
    'ku': {
        'commands': 'Ferman:',
        'enter_button': 'Fermana xwe binivîse:',
        'change_lang': 'Zimanê biguherîne',
        'wid_hei_bx': '[firehî] [bilindî] - Mezinahiya qutîkê biguherîne',
        'num_of_gen': '[hejmar] - Hejmara nifşan',
        'start': '- Otomata Şaneyê Destpê bike',
        'end': 'Dawiya nifşan',
        'enter': 'Ji bo domandinê Enterê bike',
        'gen': 'Nifş:',
        'choice_lang': 'Zimanê piştgirî hilbijêre:',
        'example_lang': 'Mînak: ji bo îngilîzî "en" binivîse',
        'seed': '[tov] - çêkirina tovê',
    },

    ## Lao
    'lo': { 
        'commands': 'ຄຳສັ່ງ:',
        'enter_button': 'ໃສ່ຄຳສັ່ງຂອງທ່ານ:',
        'change_lang': 'ປ່ຽນພາສາ',
        'wid_hei_bx': '[ຄວາມກວ້າງ] [ຄວາມສູງ] - ປ່ຽນຂະໜາດກ່ອງ',
        'num_of_gen': '[ຈຳນວນ] - ຈຳນວນລຸ້ນ',
        'start': '- ເລີ່ມຕົ້ນໂອໂຕມາຕັອນເຊວ',
        'end': 'ຈຸດຈົບຂອງລຸ້ນ',
        'enter': 'ກົດ Enter ເພື່ອດຳເນີນຕໍ່',
        'gen': 'ລຸ້ນ:',
        'choice_lang': 'ເລືອກພາສາທີ່ຮອງຮັບ:',
        'example_lang': 'ຕົວຢ່າງ: ໃສ່ "en" ສຳລັບພາສາອັງກິດ',
        'seed': '[ແກ່ນ] - ການສ້າງແກ່ນ',
    },

}