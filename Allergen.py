class Allergies(object):
    ALLERGY_SCORES = {
        'eggs': 1,
        'peanuts': 2,
        'shellfish': 4,
        'strawberries': 8,
        'tomatoes': 16,
        'chocolate': 32,
        'pollen': 64,
        'cats': 128
    }

    def __init__(self, score):
        if not type(score) == int:
            raise TypeError
        self.score = score
        self.all_list = self.calculate_allergies(score)

    def is_allergic_to(self, allergen):
        return self.all_list.__contains__(allergen)

    # alphabetically sorted
    def allergies(self):
        if len(self.all_list) == 0:
            return self.all_list
        return sorted(self.all_list)

    def calculate_allergies(self, score):
        ALLERGIES_INV = {num: value for value, num in self.ALLERGY_SCORES.items()}
        list_all = []
        binary_score = bin(score)
        for i, c in enumerate(binary_score):
            if c == '1' and ALLERGIES_INV.get(2**(len(binary_score)-i-1)):
                list_all.append(ALLERGIES_INV.get(2**(len(binary_score)-i-1)))
        return list_all




# test.describe("no_allergies_means_not_allergic")
allergies = Allergies(0)
print allergies.is_allergic_to("eggs")


allergies = Allergies(39)
print allergies.is_allergic_to("eggs")
print allergies.allergies()

# test.assert_equals(allergies.is_allergic_to('peanuts'), False)
# test.assert_equals(allergies.is_allergic_to('cats'), False)
# test.assert_equals(allergies.is_allergic_to('strawberries'), False)
#
# test.describe("is_allergic_to_eggs")
# test.assert_equals(Allergies(1).is_allergic_to('eggs'), True)
# test.assert_equals(Allergies(1).allergies(), ['eggs'])

