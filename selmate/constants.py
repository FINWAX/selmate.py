import re

WHITESPACE_PATTERN = re.compile(r'\s+')
WINDOW_LOCATION_HREF_JS_PATTERN = re.compile(r"window\.location\.href=['\"](.*?)['\"]")

CONFIRMATIONS = [
    # English
    "[x] accept all",
    "[x] accept all cookies",
    "☑️",
    "☑️ accept all",
    "☑️ accept all cookies",
    "✓",
    "✔",
    "✔ agree to all",
    "✅",
    "✅ allow all",
    "✅ allow all cookies",
    "accept",
    "accept cookies",
    "accept all",
    "accept all cookies",
    "accept and continue",
    "accept cookies and continue",
    "accept everything",
    "acknowledge",
    "acknowledged",
    "agree",
    "agree to all",
    "agree to all cookies",
    "agree to everything",
    "allow",
    "allow cookies",
    "allow all",
    "allow all cookies",
    "approve",
    "approve all",
    "approved",
    "confirm",
    "confirm cookies",
    "confirm all",
    "confirm all cookies",
    "confirmed",
    "consent",
    "consent cookies",
    "consent to all",
    "consent to all cookies",
    "consent to everything",
    "continue",
    "enter",
    "enable all",
    "enable all cookies",
    "I accept",
    "I accept cookies",
    "I accept all cookies",
    "I acknowledge",
    "I am 18 or older - Enter",
    "I am over 18",
    "I agree",
    "I agree cookies",
    "I agree all cookies",
    "I allow",
    "I allow cookies",
    "I allow all cookies",
    "I approve",
    "I confirm",
    "I confirm cookies",
    "I confirm all cookies",
    "I consent",
    "I give my consent",
    "I have read and agree",
    "I permit",
    "I understand",
    "proceed",
    "select all",
    "yes",
    "yes, continue",
    "yes, I am",
    "yes, I am under",
    "yes, I agree",
    "okay",
    "I okay",
    "alright",
    "I alright",

    # Русский
    "активировать все",
    "включить все",
    "всё принято",
    "всё понятно",
    "выбрать всё",
    "да",
    "да, согласен",
    "да, согласна",
    "даю согласие",
    "одобрить все",
    "подтверждаю",
    "подтверждение",
    "подтвердить все",
    "принимаю",
    "принимаю все",
    "принимаю условия",
    "принять всё",
    "принять все",
    "разрешаю",
    "разрешаю все",
    "разрешить все",
    "согласен",
    "согласен на обработку данных",
    "согласен со всем",
    "согласна",
    "согласие",
    "соглашаюсь",
    "согласиться со всем",
    "я даю согласие",
    "я разрешаю",
    "я соглашаюсь",
    "я согласен",
    "я согласна",
    "продолжить",
    "ок",
    "я подтверждаю",

    # Українська
    "всё прийнято",
    "все зрозуміло",
    "вибрати все",
    "дозволити все",
    "дозволяю",
    "затвердити все",
    "згоден",
    "згодна",
    "надаю згоду",
    "підтверджую",
    "погоджуюсь",
    "погоджуюсь з усім",
    "приймаю",
    "приймаю все",
    "прийняти все",
    "так",
    "так, згоден",
    "так, згодна",
    "я дозволяю",
    "я надаю згоду",
    "я погоджуюсь",
    "я підтверджую",
    "я згоден",
    "я згодна",

    # Deutsch
    "akzeptieren",
    "alle akzeptieren",
    "alle annehmen",
    "alle bestätigen",
    "alle erlauben",
    "allen zustimmen",
    "bestätigen",
    "einverstanden",
    "erlauben",
    "ich akzeptiere",
    "ich bestätige",
    "ich bin einverstanden",
    "ich erlaube",
    "ich stimme zu",
    "ja",
    "ja, ich stimme zu",
    "okay",
    "ich okay",

    # Français
    "accepté",
    "accepter tout",
    "autoriser",
    "confirmer",
    "consentir",
    "d'accord",
    "j'accepte",
    "j'autorise",
    "je confirme",
    "je consens",
    "je suis d'accord",
    "oui",
    "oui, je suis d'accord",
    "tout accepter",
    "tout autoriser",
    "approuver tout",
    "bien",
    "je bien",

    # Español
    "aceptar todo",
    "acepto",
    "aprobar todo",
    "confirmar todo",
    "consiento",
    "de acuerdo",
    "estoy de acuerdo",
    "permítir",
    "permitir todo",
    "sí",
    "sí, acepto",
    "yo permito",
    "vale",
    "está bien",

    # Italiano
    "accetta tutto",
    "accetto",
    "approva tutto",
    "confermo",
    "consento",
    "consenti a tutto",
    "sì",
    "sì, accetto",
    "sono d'accordo",
    "va bene",

    # Português
    "aceitar tudo",
    "aceito",
    "aprovar tudo",
    "concordo",
    "confirmo",
    "consinto",
    "eu aceito",
    "eu concordo",
    "permitir tudo",
    "sim",
    "sim, eu concordo",
    "tudo bem",

    # Polski
    "akceptuję",
    "potwierdzam",
    "tak",
    "tak, zgadzam się",
    "wyrażam zgodę",
    "zgoda",
    "zgoda na wszystko",
    "zaakceptuj wszystko",
    "zatwierdź wszystko",
    "dobrze",

    # Nederlands
    "accepteer",
    "akkoord",
    "alles accepteren",
    "alles goedkeuren",
    "alles toestaan",
    "bevestig",
    "ik accepteer",
    "ik bevestig",
    "ik ga akkoord",
    "oke",

    # Svenska (Swedish)
    "acceptera",
    "acceptera alla",
    "godkänn",
    "godkänn alla",
    "godkänner",
    "jag accepterar",
    "jag godkänner",
    "jag samtycker",
    "samtycke",
    "tillåt alla",
    "okej",

    # Dansk (Danish)
    "accepter",
    "accepter alle",
    "godkend",
    "godkend alle",
    "jeg accepterer",
    "jeg godkender",
    "tillad alle",
    "okay",

    # Norsk (Norwegian)
    "aksepter",
    "aksepter alle",
    "godkjenn",
    "godkjenn alle",
    "jeg aksepterer",
    "jeg godkjenner",
    "tillat alle",
    "greit",

    # Suomi (Finnish)
    "hyväksy kaikki",
    "salli kaikki",
    "ok",

    # 中文 (Chinese)
    "同意",
    "我同意",
    "接受",
    "确认",
    "好",

    # 日本語 (Japanese)
    "はい",
    "予",
    "同意する",
    "承諾する",
    "確認",
    "オーケー",

    # 한국어 (Korean)
    "동의",
    "동의합니다",
    "확인",
    "예",
    "좋아요",

    # Türkçe (Turkish)
    "evet",
    "kabul ediyorum",
    "katılıyorum",
    "onaylıyorum",
    "tamam",

    # العربية (Arabic)
    "أقر",
    "أوافق",
    "أوافق على الشروط",
    "نعم",
    "حسنا",
]
