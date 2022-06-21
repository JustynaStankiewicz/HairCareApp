import unittest
from unittest import mock
from unittest import TestCase

import Wlosy


class TestApp(TestCase):
    """
    def test_wyswietl_slownik(self):
        wlosy = Wlosy.Wlosy()
        wlosy.wyswietl_slownik("Tytuł", {"1": "jeden", "2": "dwa", "3": "trzy"})
        self.assertTrue(str(wlosy.wyswietl_slownik("Tytuł", {"1": "jeden", "2": "dwa", "3": "trzy"})).__eq__("Tytuł"
                                                                                                            "1  :  jeden"
                                                                                                             "2  :  dwa"
                                                                                                         "3  :  trzy"))
    """
    """
    @mock.patch('module_under_test.input', create=True)
    def test_znajdz_w_slowniku(self,mocked_input):
        wlosy=Wlosy.Wlosy()
        mocked_input.side_effect=["1"]
        result=wlosy.znajdz_w_slowniku({"1": "jeden", "2": "dwa", "3": "trzy"})
        self.assertEqual(result,"1 - jeden")
    """

    """
    def test_znajdz_w_slowniku_d(self):
        wlosy=Wlosy.Wlosy()
        result=str(wlosy.znajdz_w_slowniku_defult())
        self.assertFalse(result.__eq__("bad hair day - zły włosowy dzień, czyli taki, podczas którego włosy prezentują się źle lub nie chcą się układać"))
    """
    def test_znajdz_typ_skladnika_defult(self):
        wlosy=Wlosy.Wlosy()
        result=str(wlosy.znajdz_typ_skladnika_defult())
        self.assertFalse(result.__eq__("Skladnik ten nalezy do grupy protein"))

    def test_znajdz_typ_skladnika_defult2(self):
        wlosy=Wlosy.Wlosy()
        result=str(wlosy.znajdz_typ_skladnika_defult())
        self.assertFalse(result.__eq__("Skladnik ten nalezy do grupy emolientów"))

    def test_sprawdz_sklad_default(self):
        wlosy=Wlosy.Wlosy()
        result=str(wlosy.sprawdz_sklad_default())
        self.assertFalse(result.__eq__("Sklad jest humektanowy"))

    def test_sprawdz_sklad_default2(self):
        wlosy = Wlosy.Wlosy()
        result = str(wlosy.sprawdz_sklad_default())
        self.assertFalse(result.__eq__("Sklad jest emolientowy"))

if __name__ == '__main__':
    unittest.main()