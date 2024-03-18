hamburgers = ["cheese", "bulgogi"]

def format_ham(ham):
    if ham == "cheese":
        return f"{ham.title()} (Free)"
    else:
        return f"{ham.title()} ($1 Extra)"

def print_menu(hams):
    print("Welcome to visual studyria")
    print("Our available hams are:")
    for ham in hams:
        print(format_ham(ham))
        
print_menu(hamburgers)
