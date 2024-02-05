import phonebook_app


def test_phonebook_can_add_contact():
    my_phonebook = phonebook_app.Phonebook()
    my_phonebook.create_contact('dayo', '08374837483')
    assert 1 == len(my_phonebook.contact_lists)

    my_phonebook.create_contact('beejay', '08374837483')
    my_phonebook.create_contact('moh', '08374837483')
    assert 3, len(my_phonebook.contact_lists)


def test_phonebook_cant_add_number_not_up_to_eleven():
    my_phonebook = phonebook_app.Phonebook()
    my_phonebook.create_contact('dayo', '08374837')
    assert 0 == len(my_phonebook.contact_lists)