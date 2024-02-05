class Phonebook:
    contact_lists = []

    def __init__(self):
        self.contact_lists.clear()

    def create_contact(self, name, number):
        if len(number) == 11 and number[0] == "0":
            contact = {"name": name, "number": number}
            self.contact_lists.append(contact)
        else:
            return "You entered an invalid number\nContact not saved\n"

    def view_contacts(self):
        if len(self.contact_lists) == 0:
            return "There are no saved contacts"
        else:
            return self.contact_lists

    def search_contact_by_name(self, name):

        for contact in self.contact_lists:
            if contact['name'] == name:
                return f"Name: {contact['name']}\t\tNumber: {contact['number']}"
        return "Contact not found in Contact List"

    def search_contact_by_number(self, number):

        for contact in self.contact_lists:
            if contact['number'] == number:
                return f"Name: {contact['name']}\t\tNumber: {contact['number']}"

        return "Contact not found in Contact List"

    def delete_contact(self, index):
        if len(self.contact_lists) == 0:
            return "There are no contacts to delete"
        else:
            self.view_contacts()
            if 0 <= index < len(self.contact_lists):
                del self.contact_lists[index - 1]
                return "Contact deleted successfully."
            else:
                return "Invalid index"

    def display_page(self):
        while True:
            return '''\nPHONEBOOK
        1. Save a contact
        2. View Saved Contacts
        3. Search Contact
        4. Delete Contact
        5. Exit'''
            # option = int(input())
            # match option:
            #     case 1:
            #         create_contact(phonebook)
            #     case 2:
            #         view_contacts(phonebook)
            #     case 3:
            #         choose = int(input('1. Search by name\n2. Search by number: '))
            #
            #         match choose:
            #             case 1:
            #                 search_contact_by_name(phonebook, input("Enter the fullname you want to search for: "))
            #             case 2:
            #                 search_contact_by_number(phonebook, input("Enter the number you want to search for: "))
            #             case _:
            #                 print("Invalid contact")
            #
            #     case 4:
            #         delete_contact(phonebook)
            #
            #     case 5:
            #         print("Goodbye")
            #         break
            #     case _:
            #         print("Invalid option. Please try again.")
