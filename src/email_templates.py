"""
Email templates mapped to specific categories.
"""

# Category 1: Computer and Communication Technologies
TEMPLATE_COMPUTER_COMMUNICATION = {
    "subject": "Yaz Stajı Başvurusu Hakkında",
    "body": """Merhaba,

Ben Samet Cingöz. Hacettepe Üniversitesi Bilgisayar Mühendisliği 3. sınıf öğrencisiyim. Java, C++ ve Python dillerinde yazılım geliştirme; gerçek zamanlı veri işleme, ağ tabanlı veri dinleme ve masaüstü arayüz geliştirme alanlarında kendimi geliştirmekteyim.

Temmuz ayı ve sonrasında, 20–30 iş günü süreli zorunlu yaz stajımı gerçekleştirmek istiyorum. Staj süresince sigortam okulum tarafından karşılanacaktır. Şirketinizin bilgisayar ve iletişim teknolojileri alanındaki çalışmalarına yazılım geliştirme, veri görselleştirme ve sistem entegrasyonu konularında katkı sağlayabileceğimi düşünüyorum.

CV’mi ekte bilgilerinize sunuyorum. Uygun bir yaz stajı imkânı için değerlendirilmek isterim.

Gereğini arz ederim.

Saygılarımla,
Samet Cingöz
sametcingoz1@gmail.com
https://linktr.ee/scingoz
"""
}

# Category 2: Electronics
TEMPLATE_ELECTRONICS = {
    "subject": "Yaz Stajı Başvurusu Hakkında",
    "body": """Merhaba,

Ben Samet Cingöz. Hacettepe Üniversitesi Bilgisayar Mühendisliği 3. sınıf öğrencisiyim. Yazılım geliştirme, gerçek zamanlı veri işleme, ağ üzerinden veri dinleme ve görselleştirme alanlarında deneyim sahibiyim.

Temmuz ayı ve sonrasında, 20–30 iş günü süreli zorunlu yaz stajımı gerçekleştirmek istiyorum. Staj süresince sigortam okulum tarafından karşılanacaktır. Daha önce Python ve PyQt5 ile LED görselleştirme, Art-Net protokolü, DMX veri yapıları ve TCP/IP tabanlı iletişim üzerine çalıştım. Bu nedenle elektronik sistemler ile yazılımın birleştiği projelerde görev almak isterim.

CV’mi ekte bilgilerinize sunuyorum. Uygun bir yaz stajı imkânı için değerlendirilmek isterim.

Gereğini arz ederim.

Saygılarımla,
Samet Cingöz
sametcingoz1@gmail.com
https://linktr.ee/scingoz
"""
}

# Category 3: Defense Industry and Aviation
TEMPLATE_DEFENSE_AVIATION = {
    "subject": "Yaz Stajı Başvurusu Hakkında",
    "body": """Merhaba,

Ben Samet Cingöz. Hacettepe Üniversitesi Bilgisayar Mühendisliği 3. sınıf öğrencisiyim. Yazılım geliştirme, sistem programlama, gerçek zamanlı veri işleme ve proje yönetimi alanlarında kendimi geliştirmekteyim.

Temmuz ayı ve sonrasında, 20–30 iş günü süreli zorunlu yaz stajımı gerçekleştirmek istiyorum. Staj süresince sigortam okulum tarafından karşılanacaktır. Savunma sanayi ve havacılık alanındaki güvenilir, performans odaklı ve disiplinli yazılım geliştirme süreçlerinde yer almak; özellikle gerçek zamanlı sistemler, test, veri görselleştirme ve sistem entegrasyonu konularında kendimi geliştirmek isterim.

CV’mi ekte bilgilerinize sunuyorum. Uygun bir yaz stajı imkânı için değerlendirilmek isterim.

Gereğini arz ederim.

Saygılarımla,
Samet Cingöz
sametcingoz1@gmail.com
https://linktr.ee/scingoz
"""
}

# Category 4: Software
TEMPLATE_SOFTWARE = {
    "subject": "Yazılım Yaz Stajı Başvurusu Hakkında",
    "body": """Merhaba,

Ben Samet Cingöz. Hacettepe Üniversitesi Bilgisayar Mühendisliği 3. sınıf öğrencisiyim. Java, C++ ve Python dillerinde yazılım geliştirme üzerine çalışıyor; nesne yönelimli programlama, problem çözme, yazılım mühendisliği ve yapay zeka araçlarının kullanımı alanlarında kendimi geliştiriyorum.

Temmuz ayı ve sonrasında, 20–30 iş günü süreli zorunlu yaz stajımı gerçekleştirmek istiyorum. Staj süresince sigortam okulum tarafından karşılanacaktır. Şirketinizde yazılım geliştirme, backend/frontend süreçleri, test, otomasyon veya yapay zeka destekli yazılım üretimi alanlarında katkı sağlamak ve kendimi geliştirmek isterim.

CV’mi ekte bilgilerinize sunuyorum. Uygun bir yaz stajı imkânı için değerlendirilmek isterim.

Gereğini arz ederim.

Saygılarımla,
Samet Cingöz
sametcingoz1@gmail.com
https://linktr.ee/scingoz
"""
}

# Mapping of categories to templates
CATEGORY_TEMPLATES = {
    "Computer_and_Communication_Technologies": TEMPLATE_COMPUTER_COMMUNICATION,
    "Electronics": TEMPLATE_ELECTRONICS,
    "Defense_Industry_and_Aviation": TEMPLATE_DEFENSE_AVIATION,
    "Software": TEMPLATE_SOFTWARE
}

def get_template_for_category(category_name):
    """Returns the (subject, body) for a given category name."""
    template = CATEGORY_TEMPLATES.get(category_name)
    if not template:
        raise ValueError(f"No template found for category: {category_name}")
    return template["subject"], template["body"]
