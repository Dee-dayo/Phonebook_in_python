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

    def test_phonebook_can_search_by_name(self):
        my_phonebook = phonebook_app.Phonebook()
        my_phonebook.create_contact('dayo', '08374837483')
        my_phonebook.create_contact('beejay', '08374837235')
        my_phonebook.create_contact('moh', '08826384483')

        expected = 'Name: dayo\t\tNumber: 08374837483'
        self.assertEqual(expected, my_phonebook.search_contact_by_name('dayo'))

    def test_phonebook_doesnt_see_searched_name(self):
        my_phonebook = phonebook_app.Phonebook()
        my_phonebook.create_contact('dayo', '08374837483')
        my_phonebook.create_contact('beejay', '08374837235')
        my_phonebook.create_contact('moh', '08826384483')

        self.assertEqual('Contact not found in Contact List', my_phonebook.search_contact_by_name('Tobi'))

    def test_phonebook_can_search_by_number(self):
        my_phonebook = phonebook_app.Phonebook()
        my_phonebook.create_contact('dayo', '08374837483')
        my_phonebook.create_contact('beejay', '08374837235')
        my_phonebook.create_contact('moh', '08826384483')

        expected = 'Name: dayo\t\tNumber: 08374837483'
        self.assertEqual(expected, my_phonebook.search_contact_by_number('08374837483'))

    def test_phonebook_doesnt_see_searched_number(self):
        my_phonebook = phonebook_app.Phonebook()
        my_phonebook.create_contact('dayo', '08374837483')
        my_phonebook.create_contact('beejay', '08374837235')
        my_phonebook.create_contact('moh', '08826384483')

        self.assertEqual('Contact not found in Contact List', my_phonebook.search_contact_by_name('02728162765'))

    def test_phonebook_can_delete_contact(self):
        my_phonebook = phonebook_app.Phonebook()
        my_phonebook.create_contact('dayo', '08374837483')
        my_phonebook.create_contact('beejay', '08374837235')
        self.assertEqual(2, len(my_phonebook.contact_lists))

        my_phonebook.delete_contact(1)
        self.assertEqual(1, len(my_phonebook.contact_lists))

    def test_phonebook_has_display_page(self):
        my_phonebook = phonebook_app.Phonebook()

        expected = '''\nPHONEBOOK
        1. Save a contact
        2. View Saved Contacts
        3. Search Contact
        4. Delete Contact
        5. Exit'''
        self.assertEqual(expected, my_phonebook.display_page())
