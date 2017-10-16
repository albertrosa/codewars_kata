import unittest


def spin_words(sentence):
    words = sentence.split(" ")
    final = ""
    for word in words:
        if word.__len__() >= 5:
            letters = list(word)
            letters.reverse()
            final = "%s %s" % (final, "".join(letters))
        else:
            final = "%s %s" % (final, word)
    return final.strip()


class TestSpinWords(unittest.TestCase):

    def test_spin_words(self):
        self.assertEqual(spin_words("Welcome"), "emocleW")
        self.assertEqual(spin_words( "Hey fellow warriors" ),"Hey wollef sroirraw")
        self.assertEqual(spin_words( "This is a test"), "This is a test")
        self.assertEqual(spin_words( "This is another test" ), "This is rehtona test")

