import unittest
import re


def increment_string(text):
    regexWordsOnly = '^([a-zA-Z]+)'
    word = re.compile(regexWordsOnly)
    word_result = word.search(text)

    regexNumbersOnly = '(\d+)'
    numbers = re.compile(regexNumbersOnly)
    numbers_result = numbers.search(text)

    regexUnicode = '(u[0-9]+)$'
    unicodes = re.compile(regexUnicode)
    unicodes_result = unicodes.search(text)

    lettersAfterNumber = '([0-9]+)([a-zA-Z]+)'
    numLeters = re.compile(lettersAfterNumber)
    numLeters_result = numLeters.search(text)

    if numbers_result:
        current_number = numbers_result.group()
        num = str(int(current_number) + 1)

        while current_number.__len__() > num.__len__():
            num = "0" + num

        if word_result and (unicodes_result or numLeters_result):
            return word_result.group() + num + "0"
        elif word_result:
            return word_result.group() + num
        elif unicodes_result:
            return num + "0"
        else:
            return num
    else:
        return text + "1"


class TestIncrementString(unittest.TestCase):

    def test_increment_string(self):
        self.assertEqual(increment_string("foo"), "foo1")
        self.assertEqual(increment_string("foobar001"), "foobar002")
        self.assertEqual(increment_string("foobar1"), "foobar2")
        self.assertEqual(increment_string("foobar00"), "foobar01")
        self.assertEqual(increment_string("foobar99"), "foobar100")
        self.assertEqual(increment_string("foobar099"), "foobar100")
        self.assertEqual(increment_string(""), "1")
        self.assertEqual(increment_string("32"), "33")
        self.assertEqual(increment_string("D4723057628"), "D4723057629")
        self.assertEqual(increment_string("144014T830557/)5z:u089"), "1440150")
        self.assertEqual(increment_string("i]n)?NK48SxV<^(r627847585H\kPL3717038020784QO314|ZcXKO?0909689"), "i490")

