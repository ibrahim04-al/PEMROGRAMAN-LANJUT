def main():
    try:
        f = open("data.txt", "w")

        try:
            f.erite("pemrograman python")
        finally:
            f.close()
    except IOError:
        print("\nERROR: File tidak dapat " +
              "dibuka/ditulis")

if __name__ == "__main__":
    main()
