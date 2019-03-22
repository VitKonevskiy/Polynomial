import unittest
from Polynomial import Polynomial


class PolynomialTests(unittest.TestCase):
    def test_CheckTypeError(self):
        self.assertRaises(TypeError, Polynomial, ['q'])
        self.assertRaises(TypeError, Polynomial, [0.11])
        self.assertRaises(TypeError, Polynomial, [])
        self.assertRaises(TypeError, Polynomial, ['u', 54])
        self.assertRaises(TypeError, Polynomial.__add__, Polynomial([1, 2, 3]), "w")
        self.assertRaises(TypeError, Polynomial.__mul__, Polynomial([1, 2]), "w")
        self.assertRaises(TypeError, Polynomial.__eq__, Polynomial([1, 2]), "w")

    def test_AddPos(self):
        p = Polynomial([3, 9, 6, 9])
        s = Polynomial([1, 4, 6])
        self.assertListEqual((p + s).coeffList, [3, 10, 10, 15])
        self.assertListEqual((s + p).coeffList, [3, 10, 10, 15])

    def test_AddPosNeg(self):
        p = Polynomial([-1, 3, -6, 9])
        s = Polynomial([5, 4, 5])
        self.assertListEqual((p + s).coeffList, [-1, 8, -2, 14])
        self.assertListEqual((s + p).coeffList, [-1, 8, -2, 14])

    def test_AddPosNegConst(self):
        p = Polynomial([-1, 4, -6, 9])
        self.assertListEqual((p + 6).coeffList, [-1, 4, -6, 15])
        self.assertListEqual((p - 11).coeffList, [-1, 4, -6, -2])

    def test_AddPosNegNull(self):
        p = Polynomial([0, 0, 0, -1, 0, 4, 0, -6, 9])
        s = Polynomial([0, 0, 0, 0, 0, 1, 4])
        self.assertListEqual((p + s).coeffList, [-1, 0, 4, 0, -5, 13])
        self.assertListEqual((s + p).coeffList, [-1, 0, 4, 0, -5, 13])

    def test_AddZero(self):
        p = Polynomial([0, 0, 0, -1, 0, 4, 0, -6, 9])
        s = Polynomial([0, 0, 0])
        self.assertListEqual((p + s).coeffList, [-1, 0, 4, 0, -6, 9])

    def test_AddConst(self):
        p = Polynomial([0, 0, 0, -1, 0, 4, 0, -6, 9])
        s = 5
        self.assertListEqual((p + s).coeffList, [-1, 0, 4, 0, -6, 14])

    def test_LeftAddConst(self):
        p = Polynomial([0, 0, 0, -1, 0, 4, 0, -6, 9])
        s = 5
        self.assertListEqual((s + p).coeffList, [-1, 0, 4, 0, -6, 14])

    def test_Sub(self):
        p = Polynomial([0, 0, 0, -1, 0, 5, 0, -6, 10])
        s = Polynomial([0, 0, 0, 0, 0, 1, 4])
        self.assertListEqual((p - s).coeffList, [-1, 0, 5, 0, -7, 6])
        self.assertListEqual((s - p).coeffList, [1, 0, -5, 0, 7, -6])

    def test_Mult(self):
        p = Polynomial([0, 0, 0, -1, 0, 5, 0, -6, 10])
        s = Polynomial([0, 0, 0, 0, 0, 1, 4])
        self.assertListEqual((p * s).coeffList, (s * p).coeffList)
        p = Polynomial([1, -1, 1])
        s = Polynomial([-1, 1])
        self.assertEqual((p * s).coeffList, [-1, 2, -2, 1])

    def test_MultZero(self):
        p = Polynomial([1, -1, 1])
        s = Polynomial([0, 0])
        self.assertEqual((p * s).coeffList, [0])

    def test_MultConst(self):
        p = Polynomial([6, -1, 4])
        s = 5
        self.assertEqual((s * p).coeffList, [30, -5, 20])

    def test_LeftMultConst(self):
        p = Polynomial([5, -1, 1])
        s = 5
        self.assertEqual((p * s).coeffList, [25, -5, 5])

    def test_Str(self):
        p = Polynomial([-1, -4, 0])
        self.assertEqual(str(p), "- x^2 - 4x")
        p = Polynomial([-1, -4, -6])
        self.assertEqual(str(p), "- x^2 - 4x - 6")
        p = Polynomial([0])
        self.assertEqual(str(p), "0")
        p = Polynomial([0, 0, 0])
        self.assertEqual(str(p), "0")
        p = Polynomial([1, 4, 9])
        self.assertEqual(str(p), "x^2 + 4x + 9")
        p = Polynomial([1, 0, 4])
        self.assertEqual(str(p), "x^2 + 4")
        p = Polynomial([-1, 4, -1])
        self.assertEqual(str(p), "- x^2 + 4x - 1")

    def test_EqualInt(self):
        p = Polynomial([1, 4, 6])
        s = Polynomial([0, 0, 0, 0, 0, 1, 4])
        self.assertEqual(p, Polynomial([1, 4, 6]))
        self.assertTrue(p == Polynomial([1, 4, 6]))
        self.assertTrue(p != s)
        self.assertFalse(p == s)
        s = Polynomial([0, 0, 0, 0, 0])
        p = 0
        self.assertTrue(p == s)

    def test_PrintInternalView(self):
        p = Polynomial([-1, -2, 0])
        self.assertEqual(p.printInternalView(), "Polynomial([-1, -2, 0])")
        p = Polynomial([-1, -4, -4])
        self.assertEqual(p.printInternalView(), "Polynomial([-1, -4, -4])")
        p = Polynomial([0])
        self.assertEqual(p.printInternalView(), "Polynomial([0])")
        p = Polynomial([0, 0, 0])
        self.assertEqual(p.printInternalView(), "Polynomial([0])")
        p = Polynomial([1, 4, 9])
        self.assertEqual(p.printInternalView(), "Polynomial([1, 4, 9])")
        p = Polynomial([1, 0, 4])
        self.assertEqual(p.printInternalView(), "Polynomial([1, 0, 4])")
        p = Polynomial([-1, 4, -7])
        self.assertEqual(p.printInternalView(), "Polynomial([-1, 4, -7])")

if __name__ == '__main__':
    unittest.main()