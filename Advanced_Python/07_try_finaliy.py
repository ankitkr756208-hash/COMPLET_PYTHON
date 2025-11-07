def main():
    
    try:
        a=int(input("Enter the number:"))
        print(a)
        return

    except Exception as e:
        print(e)
        return

    else:
        print("No exception occurred. The input number is:", a)
    finally:
        print("Execution of try-except-else block is complete.")

main()