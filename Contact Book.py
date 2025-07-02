print("--------CONTACT BOOK----------")
contact={}
def display_contact():
    print(contact.items())
    print("Name\t\tContact Number")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))
while True:
    choice = int(input("1.Add new contact\n2.Search contact \n3.Display contact\n4.Edit contact\n5.Delete contact\n6.Exit\n Enter your choice:"))
    if choice == 1:                                                                                               #Add contact
        name = input("enter the contact name:")
        phone = input("enter the mobile number:")
        contact[name] = phone

    elif choice == 2:                                                                                             #search contact
        search_name = input("enter the contact name:")
        if search_name in contact:
            print(search_name,"'s contact number is ",contact[search_name])
        else:
            print("Name is not found in contact book:")

    elif choice == 3:                                                                                            #Display contact
        if not contact:
            print("contact book is empty:")
        else:
            display_contact()

    elif choice == 4:                                                                                             #Edit contact
        edit_contact = input("Enter the contact to be edited:")
        if edit_contact in contact:
            phone = input("enter mobile number:")
            contact[edit_contact]=phone
            print("contact is updated:")
            display_contact()
        else:
            print("Name is not found in contact book:")

    elif choice == 5:                                                                                           #Delete contact
        del_contact = input("Enter the contact to be deleted:")
        if del_contact in contact:
            confirm = input("Do you want to delete this contact y/n? ")
            if confirm =='y':
                contact.pop(del_contact)
            display_contact()
        else:
            print("Name is not found in contact book:")
    else:
        break
