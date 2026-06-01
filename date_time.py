from datetime import date
import inflect

def main():
    try:
        birthday = date.fromisoformat(input("Date of Birth: "))
    except ValueError:
        print("Invalid date")
        return

    today = date.today()
    minutes = (today - birthday).days * 24 * 60

    p = inflect.engine()
    print(p.number_to_words(minutes, andword="").capitalize() + " minutes")

main()