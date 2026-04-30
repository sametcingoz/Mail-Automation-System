import unittest
from src.email_templates import get_template_for_category

class TestEmailTemplates(unittest.TestCase):
    def test_get_template_for_category_valid(self):
        subject, body = get_template_for_category("Software")
        self.assertEqual(subject, "Yazılım Yaz Stajı Başvurusu Hakkında")
        self.assertIn("Samet Cingöz", body)
        self.assertIn("Yazılım geliştirme", body)

    def test_get_template_for_category_invalid(self):
        with self.assertRaises(ValueError):
            get_template_for_category("InvalidCategory")

if __name__ == '__main__':
    unittest.main()
