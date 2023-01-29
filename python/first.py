def main():
    print("Weng Davo")
    print("Pyhton")
    value = int(input("Rate this work:"))
    msg_good = "Thank you "
    msg_bad = "I'll do better next time "
    msg = msg_good if value > 50 else msg_bad
    print(msg)

if __name__ == "__main__":
    main()

