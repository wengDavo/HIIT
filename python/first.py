def main():
    print("Weng Davo")
    print("Software Engineering")
    value = int(input("Rate this work:"))
    msg_good = "Thank you for giving my work a rating of ",value
    msg_bad = "Wow you gave my working a rate of ",value
    print(msg_good if value > 50 else msg_bad)

if __name__ == "__main__":
    main()

