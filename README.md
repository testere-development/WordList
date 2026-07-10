# TESTERE WordList

Şəxsi məlumatlara əsaslanaraq hədəflənmiş (targeted) parol siyahısı (wordlist) yaradan Python skripti. Sosial mühəndislik / OSINT əsaslı pentest ssenarilərində istifadə üçün nəzərdə tutulub — CUPP kimi alətlərə bənzər məntiqlə işləyir.

```
[ TESTERE ]
--------------
w o r d l i s t
------------aze
```

## Xüsusiyyətlər

Skript işə düşəndə 3 rejimdən birini seçməyə imkan verir:

1. **Şəxsə özəl (Şəxsi məlumat əsaslı)** — Ad, soyad, ləqəb, doğum tarixi, ana/ata adı və doğum tarixləri, yoldaş/uşaq adı və tarixləri, ev heyvanı, ölkə, şəhər, kənd, telefon və maşın nömrəsi kimi sahələri soruşur. Bu dəyərləri (və doğum tarixlərindən çıxarılan gün/ay/il hissələrini) bir-biri ilə və ümumi son əlavələrlə (`123`, `admin`, `!`, `qwerty` və s.) müxtəlif kombinasiyalarda (böyük/kiçik hərf, `_`, `.`, `-` ayırıcıları ilə) birləşdirərək wordlist yaradır.
2. **İl + İl** — 1900–2050 aralığındakı illəri cüt-cüt müxtəlif ayırıcılarla (`_`, `.`, `-`, boşluqsuz) kombinasiya edərək wordlist yaradır. İstəyə görə əlavə "salt" simvolu da qatıla bilər.
3. **Başlanğıc + Random + Son** — İstifadəçinin verdiyi prefiks və suffiks arasına rəqəm, hərf və ya rəqəm+hərf kombinasiyasından təsadüfi (random) simvollar əlavə edərək bruteforce tipli wordlist yaradır.

Bütün rejimlərdə minimum/maksimum parol uzunluğu təyin edilə bilər və nəticə `.txt` faylına yazılır.

## Tələblər

- Python 3.x
- Əlavə kitabxana tələb olunmur (yalnız standart kitabxana: `random`, `sys`)

## İstifadə

```bash
python WordList.py
```

Skript işə düşdükdən sonra ekrandakı sualları addım-addım cavablandırın:

```
Max Carakter (default 8):
Min Cakrakter (default 0):

1.Şəxsə özəl
2.Il+il
3.Başlanğıc+Random+Son
=>
```

Seçdiyiniz rejimə uyğun suallar davam edəcək. Proses bitdikdə fayl adı və yaradılan sözlərin sayı ekrana çıxır:

```
WordList:
    File Name : ad.txt
    File Len: 12480
```

## Çıxış nümunəsi

| Rejim | Çıxış faylı |
|---|---|
| Şəxsə özəl | `<ad>.txt` |
| İl + İl | `yearWordList.txt` |
| Başlanğıc+Random+Son | `startEnd_WordList.txt` |

## Qeydlər

- Böyük wordlist-lər (xüsusilə "İl+İl" və "Random" rejimləri) yüksək `Max Carakter` dəyərlərində çox böyük fayl və uzun icra vaxtı yarada bilər.
- Bu alət yalnız **qanuni icazəli** pentest, təhlükəsizlik testi və ya öz məlumatlarınız üzərində tədqiqat məqsədilə istifadə üçün nəzərdə tutulub. Başqasının icazəsi olmadan onun məlumatları əsasında parol siyahısı yaratmaq və istifadə etmək qanunsuzdur.

## Lisenziya

Bu layihəyə uyğun lisenziyanı özünüz seçib əlavə edə bilərsiniz (məs: MIT).
