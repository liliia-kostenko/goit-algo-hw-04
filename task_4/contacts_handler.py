def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command. Format: add [username] [phone]"
    username, phone = args
    contacts[username] = phone
    return f"Contact {username} added."

def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command. Format: change [username] [new phone]"
    username, phone = args
    if username not in contacts:
        return f"Contact {username} not found."
    contacts[username] = phone
    return f"Contact {username} updated."

def show_phone(args, contacts):
    if len(args) != 1:
        return "Invalid command. Format: phone [username]"
    username = args[0]
    if username not in contacts:
        return f"Contact {username} not found."
    return f"for {username} number - {contacts[username]}"

def show_all(contacts):
    if not contacts:
        return "No contacts found."
    all_contacts = "\n".join([f"{username}: {phone}" for username, phone in contacts.items()])
    return all_contacts
