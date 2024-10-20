#write functions here, don't add input('') statements here!
def test_config():
    return True

def get_miles_per_hour (kilometers, minutes):
    if kilometers < 0 or minutes < 0:
        return 'Invalid arguments'
    
    conv = 0.621371
    miles = kilometers * conv
    
    hours = min /60
    miles_per_hour = miles / hours

    return miles_per_hour

if __name__ == "__main__":
    kilometers = int(input("Enter Kilometers: "))
    minutes = int(input("Enter Minutes: "))

    result = get_miles_per_hour(kilometers, minutes)

    print (result)