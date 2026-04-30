"""
Email templates mapped to specific categories.
"""

# Category 1: Computer and Communication Technologies
TEMPLATE_COMPUTER_COMMUNICATION = {
    "subject": "Yaz Stajı Başvurusu Hakkında",
    "body": """Merhaba,

Ben...

Gereğini arz ederim.

Saygılarımla,
@gmail.com
"""
}

# Category 2: Electronics
TEMPLATE_ELECTRONICS = {
    "subject": "Yaz Stajı Başvurusu Hakkında",
    "body": """Merhaba,

Ben...

Gereğini arz ederim.

Saygılarımla,
@gmail.com
"""
}

# Category 3: Defense Industry and Aviation
TEMPLATE_DEFENSE_AVIATION = {
    "subject": "Yaz Stajı Başvurusu Hakkında",
    "body": """Merhaba,

Ben...

Gereğini arz ederim.

Saygılarımla,
@gmail.com
"""
}

# Category 4: Software
TEMPLATE_SOFTWARE = {
    "subject": "Yazılım Yaz Stajı Başvurusu Hakkında",
    "body": """Merhaba,

Ben...

Gereğini arz ederim.

Saygılarımla,
@gmail.com
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
