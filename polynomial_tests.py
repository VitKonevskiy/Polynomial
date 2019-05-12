import unittest
from polynomial import Polynomial


class PolynomialTests(unittest.TestCase):
    def test_check_type_error(self):
        self.assertRaises(TypeError, Polynomial, ['q'])
        self.assertRaises(TypeError, Polynomial, [0.11])
        self.assertRaises(TypeError, Polynomial, [])
        self.assertRaises(TypeError, Polynomial, ['u', 54])
        self.assertRaises(TypeError, Polynomial.__add__, Polynomial([1, 2, 3]), "w")
        self.assertRaises(TypeError, Polynomial.__mul__, Polynomial([1, 2]), "w")
        self.assertRaises(TypeError, Polynomial.__eq__, Polynomial([1, 2]), "w")

    def test_init_copy_polynom(self):
        p = Polynomial([3, 9, 6])
        test = Polynomial(p)
        self.assertListEqual(test.coeffs, p.coeffs)
        test.coeffs[0] = test.coeffs[0] + 4
        self.assertNotEqual(test.coeffs[0], p.coeffs[0])
        test.coeffs.append(9)
        self.assertNotEqual(len(test.coeffs), len(p.coeffs))

    def test_add_pos(self):
        p = Polynomial([3, 9, 6, 9])
        s = Polynomial([1, 4, 6])
        self.assertListEqual((p + s).coeffs, [3, 10, 10, 15])
        self.assertListEqual((s + p).coeffs, [3, 10, 10, 15])

    def test_add_pos_neg(self):
        p = Polynomial([-1, 3, -6, 9])
        s = Polynomial([5, 4, 5])
        self.assertListEqual((p + s).coeffs, [-1, 8, -2, 14])
        self.assertListEqual((s + p).coeffs, [-1, 8, -2, 14])

    def test_add_pos_neg_const(self):
        p = Polynomial([-1, 4, -6, 9])
        self.assertListEqual((p + 6).coeffs, [-1, 4, -6, 15])
        self.assertListEqual((p - 11).coeffs, [-1, 4, -6, -2])

    def test_add_pos_neg_null(self):
        p = Polynomial([0, 0, 0, -1, 0, 4, 0, -6, 9])
        s = Polynomial([0, 0, 0, 0, 0, 1, 4])
        self.assertListEqual((p + s).coeffs, [-1, 0, 4, 0, -5, 13])
        self.assertListEqual((s + p).coeffs, [-1, 0, 4, 0, -5, 13])

    def test_add_zero(self):
        p = Polynomial([0, 0, 0, -1, 0, 4, 0, -6, 9])
        s = Polynomial([0, 0, 0])
        self.assertListEqual((p + s).coeffs, [-1, 0, 4, 0, -6, 9])

    def test_add_const(self):
        p = Polynomial([0, 0, 0, -1, 0, 4, 0, -6, 9])
        s = 5
        self.assertListEqual((p + s).coeffs, [-1, 0, 4, 0, -6, 14])

    def test_left_add_const(self):
        p = Polynomial([0, 0, 0, -1, 0, 4, 0, -6, 9])
        s = 5
        self.assertListEqual((s + p).coeffs, [-1, 0, 4, 0, -6, 14])

    def test_sub(self):
        p = Polynomial([0, 0, 0, -1, 0, 5, 0, -6, 10])
        s = Polynomial([0, 0, 0, 0, 0, 1, 4])
        self.assertListEqual((p - s).coeffs, [-1, 0, 5, 0, -7, 6])
        self.assertListEqual((s - p).coeffs, [1, 0, -5, 0, 7, -6])

    def test_mult(self):
        p = Polynomial([0, 0, 0, -1, 0, 5, 0, -6, 10])
        s = Polynomial([0, 0, 0, 0, 0, 1, 4])
        self.assertListEqual((p * s).coeffs, (s * p).coeffs)
        p = Polynomial([1, -1, 1])
        s = Polynomial([-1, 1])
        self.assertEqual((p * s).coeffs, [-1, 2, -2, 1])
        self.assertEqual(p.coeffs, [1, -1, 1])
        self.assertEqual(s.coeffs, [-1, 1])

    def test_mult_zero(self):
        p = Polynomial([1, -1, 1])
        s = Polynomial([0, 0])
        self.assertEqual((p * s).coeffs, [0])

    def test_mult_const(self):
        p = Polynomial([6, -1, 4])
        s = 5
        self.assertEqual((s * p).coeffs, [30, -5, 20])

    def test_left_mult_const(self):
        p = Polynomial([5, -1, 1])
        s = 5
        self.assertEqual((p * s).coeffs, [25, -5, 5])

    def test_str(self):
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
        p = Polynomial([-1, 4, -1, 5, 1, 2, -5])
        self.assertEqual(str(p), "- x^6 + 4x^5 - x^4 + 5x^3 + x^2 + 2x - 5")

    def test_equal_int(self):
        p = Polynomial([1, 4, 6])
        s = Polynomial([0, 0, 0, 0, 0, 1, 4])
        self.assertEqual(p, Polynomial([1, 4, 6]))
        self.assertTrue(p == Polynomial([1, 4, 6]))
        self.assertTrue(p != s)
        self.assertFalse(p == s)
        s = Polynomial([0, 0, 0, 0, 0])
        p = 0
        self.assertTrue(p == s)

    def test_print_internal_view(self):
        p = Polynomial([-1, -2, 0])
        self.assertEqual(repr(p), "Polynomial([-1, -2, 0])")
        p = Polynomial([-1, -4, -4])
        self.assertEqual(repr(p), "Polynomial([-1, -4, -4])")
        p = Polynomial([0])
        self.assertEqual(repr(p), "Polynomial([0])")
        p = Polynomial([0, 0, 0])
        self.assertEqual(repr(p), "Polynomial([0])")
        p = Polynomial([1, 4, 9])
        self.assertEqual(repr(p), "Polynomial([1, 4, 9])")
        p = Polynomial([1, 0, 4])
        self.assertEqual(repr(p), "Polynomial([1, 0, 4])")
        p = Polynomial([-1, 4, -7])
        self.assertEqual(repr(p), "Polynomial([-1, 4, -7])")

    def test_double_negation(self):
        p = Polynomial([-1, -2, 0])
        p1 = Polynomial([-1, -4, -4])
        self.assertFalse(p == p1)
        self.assertTrue(p != p1)
        self.assertFalse(not (p != p1))


if __name__ == '__main__':
    unittest.main()

