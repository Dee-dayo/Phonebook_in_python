import phonebook_app


def test_phonebook_can_add_contact():
    my_phonebook = phonebook_app.Phonebook()
    my_phonebook.create_contact('dayo', '08374837483')
    assert 1 == len(my_phonebook.contact_lists)

    # my_phonebook.create_contact('beejay', '08374837483')
    # my_phonebook.create_contact('moh', '08374837483')
    # self.assertEqual(3, len(my_phonebook.contact_lists))