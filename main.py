try:
    f =open("index.py")
    try:
        f.write("Hello its Gibson")
    except:
        print("Something went wrong when writting to the file")
    finally:
        f.close()
    except:
        print("Something went wrong when opening the file")