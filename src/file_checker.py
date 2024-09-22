import protocol as pr

def files_to_rename(items):

    items_to_rename = []
    for item in items:
    
        if not (pr.verify_protocol(item)):
            print(f"{item} have to be named")
            items_to_rename.append(item)
        
    return items_to_rename