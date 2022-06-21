

response_code = 400

match response_code:
    case 200:
        print("Everything's peachy!")
    case 300:
        print("You're going somewhere else!")
    case 400:
        print("Uh oh. Are you lost?")
    case 500:
        print("Yikes. Something went wrong!")

