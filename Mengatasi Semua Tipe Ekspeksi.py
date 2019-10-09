def main():

    print("PROGRAM PEMBAGIAN BILANGAN")

    try:
        a = float(input("masukkan a: "))
        b = float(input("masukkan b: "))

        hasil = a / b

    except(ZeroDivisionError, ValueError,
           KeyboardInterrupt):
        print("\nERROR: Anda telah melakukan " +
              "kesalahan")

    else:
         print("\na : ", a)
         print("b : ", b)
         print("a / b = ", hasil)

if __name__ == "__main__":
    main()
