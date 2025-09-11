seat_type = input("enter seat type (sleeper/AC/general/luxury)").lower()

match seat_type:
    case "sleeper":
        print("you chooser spleeper")
    case "ac":
        print("you chooser AC")
    case "general":
        print("you choose general")
    case "luxury":
        print("you choose luxury")
    case default:
        print("you did not choose any seat")
