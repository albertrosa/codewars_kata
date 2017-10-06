import unittest

geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]


def goose_filter(birds):
    final = []
    for bird in birds:
        if bird not in geese:
            final.append(bird)
    return final


class TestGooseFilter(unittest.TestCase):

    def test_filter(self):
        self.assertEquals(
            goose_filter(["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]),
            ["Mallard", "Hook Bill", "Crested", "Blue Swedish"])
        self.assertEquals(goose_filter(["Mallard", "Barbary", "Hook Bill", "Blue Swedish", "Crested"]),
                           ["Mallard", "Barbary", "Hook Bill", "Blue Swedish", "Crested"])
        self.assertEquals(goose_filter(["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]), [])