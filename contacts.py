"""
TASK: Create a ContactBook class.

Requirements:
1. Store contacts in a dictionary (name → phone number).
2. Provide a method to add new contacts.
3. Provide a method to delete contacts.
4. Provide a method to search for a contact by name.
5. Provide a method to show all contacts.

Example Usage:
    book = ContactBook()
    book.add_contact("Alice", "08012345678")
    print(book.search_contact("Alice"))  # "08012345678"
"""
class Contacts:
    def __init__(self,contact):
        self.contact = {'Akila':'09043430332','Amala':'2203044030','Bala':'0430030466'}
    def add_contact(self,new_contact):
        return self.add_contact.update({'new_contact'})
    def search(self,check):
        return self.contact.get('item')
contact = Contacts(1)
print(contact.contact)
print(contact.search('Akila'))