from models.medicine import Medicine
from models.grocery import Grocery
from models.documents import Document


def main():

    medicine = Medicine(
        1,
        "Paracetamol",
        10,
        "20-07-2026",
        "Cipla",
        "500 mg"
    )

    grocery = Grocery(
        2,
        "Rice",
        2,
        "25-12-2026",
        "5 kg"
    )

    document = Document(
        3,
        "Passport",
        1,
        "20-01-2030",
        "Government of India"
    )

    medicine.display()
    print("-" * 40)

    grocery.display()
    print("-" * 40)

    document.display()


if __name__ == "__main__":
    main()