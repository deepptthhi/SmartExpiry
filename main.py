from models.medicine import Medicine


def main():

    med = Medicine(
        1,
        "Paracetamol",
        10,
        "20-07-2026",
        "Cipla",
        "500 mg"
    )

    med.display()

    print("Expired :", med.is_expired())


if __name__ == "__main__":
    main()