def main():

    print("PROGRAM PEMBAGIAN BILANGAN")

    a = float(input("Masukkan a: "))
    b = float(input("masukkan b: "))

    try:
        hasil = a / b
    except ZeroDivisionError:
        print("\nERROR: Nilai b tidak boleh nol")
    else:
        print("\na : ", a)
        print(" : ", b)
        print("a / = ", hasil)

if __name__ == "__main__":
    main()
