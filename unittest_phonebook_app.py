import unittest

import phonebook_app


class MyTestCase(unittest.TestCase):
    def test_phonebook_can_add_contact(self):
        my_phonebook = phonebook_app.Phonebook()
        my_phonebook.create_contact('dayo', '08374837483')
        self.assertEqual(1, len(my_phonebook.contact_lists))

        my_phonebook.create_contact('beejay', '08374837483')
        my_phonebook.create_contact('moh', '08374837483')
        self.assertEqual(3, len(my_phonebook.contact_lists))

    def test_phonebook_cant_add_number_not_up_to_eleven(self):
        my_phonebook = phonebook_app.Phonebook()
        my_phonebook.create_contact('dayo', '08374837')
        self.assertEqual(0, len(my_phonebook.contact_lists))

    def test_phonebook_cant_add_number_that_doesnt_start_with_zero(self):
        my_phonebook = phonebook_app.Phonebook()
        my_phonebook.create_contact('dayo', '74837483')
        self.assertEqual(0, len(my_phonebook.contact_lists))

    def test_phonebook_can_view_all_contacts(self):
        my_phonebook = phonebook_app.Phonebook()
        my_phonebook.create_contact('dayo', '08374837483')

        saved = [{'name':'dayo', 'number':'08374837483'}]
        self.assertEqual(saved, my_phonebook.view_contacts())

        my_phonebook.create_contact('beejay', '08374837235')
        my_phonebook.create_contact('moh', '08826384483')

        new_saved = [{'name':'dayo', 'number':'08374837483'}, {'name':'beejay', 'number':'08374837235'},
{'name':'moh', 'number': '08826384483'}]
        self.assertEqual(new_saved, my_phonebook.view_contacts())