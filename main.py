# Function that will ask the user to enter the data for his specific use case:
def get_data():
    # Boolean variables:
    ttc = True # Assume people use the ttc to get to Campus from Union Station
    localtransit = True # Assume people use local transit to get to their Go Train Station
    timesbool = False # Boolean used in while loop to make sure user enters an int value
    # Some local variables used as index values for future operations:
    # These two fare indexes are going to determine the fare of the Go train
    fareindex = 0
    fareindex2 = 0
    trainindex = 0 # Index that will be used for determining the train line user takes
    times = 8
    print("This program will calculate how much transportation is going to cost for any Ryerson student who commutes to the university using the Go Train System each month")
    print("(Assuming they use a PRESTO card)")
    print()
    print("Which Train line do you take?")
    print("Train lines available are:")
    print(trains)
    trainline = input("Enter your train line: ")
    # Error catching if user does not enter a valid input
    while(trainline not in trains):
        print("Invalid Input")
        print("Please enter a valid train line.")
        print("Train lines available are:")
        print(trains)
        trainline = input("Enter your train line: ")
    print(f"You selected {trainline}, Which station do you get on?")
    print("Stations available are:")
    # Loop that will go through all train lines until it finds yours, then it prints the stations for said line:
    for i in range(len(trains)):
        if(trainline == trains[i]):
            trainindex = i
            print(trainstations[i])
    station = input("Enter your station: ")
    # Error catching if user does not enter a valid input
    while(station not in trainstations[trainindex]):
        print("Invalid Input")
        print("Please enter a valid train line.")
        print("Train lines available are:")
        print(trainstations[trainindex])
        station = input("Enter your station: ")
    # This loop will correlate both lists (trainstations and fares) in order to determine which fare corresponds to user's train station:
    for line in trainstations:
        for stationf in line:
            if(stationf == station): # Loop has found your train station
                # Using the indexes previously declared it will generate a new list containing all the fares of your train line and subsequently find the fare corresponding to your station:
                fareline = fares[fareindex]
                fare = fareline[fareindex2]
            fareindex2 +=1
        fareindex +=1
        fareindex2 = 0 # Reset the fareindex2 to 0 because it did not find a match in this train line
    # Error catching this will ask the user to enter an int value and check whether or not the user entered an int value
    while(timesbool == False):
        times = input("How many times a week do you go to campus? ")
        try:
            times = int(times)
            if(times > 7):
                print("You cannot go to campus more than 7 times a week (There are only 7 days in a week).")
                continue
            elif(times < 0):
                print("You cannot go to campus a negative amount of times.")
                continue
            timesbool = True
        except ValueError:
            print("Invalid input")
            print("Please enter an integer value.")
            print("You cannot go to campus more than 7 times a week (There are only 7 days in a week)")
    # Error catching will ask the user to enter either "Yes" or "No" and print invalid input if something else is entered
    ttcinput = input("Do you use the TTC subway to get from Union Station to campus? 'Yes'/'No': ")
    while(ttcinput != "Yes" and ttcinput != "No"):
        print("Invalid Input")
        print("Valid Inputs are 'Yes' or 'No'")
        ttcinput = input("Do you use the TTC subway to get from Union Station to campus? 'Yes'/'No': ")
    if(ttcinput == "No"):
        ttc = False # Default answer was set to True, so if "No" is inputted change to False
    # Error catching will ask the user to enter either "Yes" or "No" and print invalid input if something else is entered
    localtransitinput = input("Do you use local transit to get to your Go Train Station? 'Yes'/'No': ")
    while (localtransitinput != "Yes" and localtransitinput != "No"):
        print("Invalid Input")
        print("Valid Inputs are 'Yes' or 'No'")
        localtransitinput = input("Do you use local transit to get to your Go Train Station? 'Yes'/'No': ")
    if (localtransitinput == "No"):
        localtransit = False  # Default answer was set to True, so if "No" is inputted change to False
    return trainline, station, fare, times, ttc, localtransit

# Function where all the actual math operations will take place:
def calculate_trans():
    # Call for get_data function and use the values it generates to perform future calculations:
    line, station, fare, times, ttc, localtransit = get_data()
    times  = (times*2)*4 # Calculate how many times a month user uses transportation based on inputted value
    ttcfare = 2.25
    monthly_cost = 0 # Montly cost is initialized as 0
    # The three following if/else account for all possible variants(ie. User takes the subway or not, uses local transit or not)
    # The way Go Transit calculates your fare is by the number is instances you use Go Train a month
    # If you use Go Train 1 to 30 times in a month you pay full fare
    # If you use Go Train between 31 and 40 times in a month your fare drops 91.84%
    # If you use Go Train more than 40 times you ride for free
    if(ttc == True):
        if(times <= 30): # User rides less than 31 times a month so pays full fare
            monthly_cost = fare*times + ttcfare*times
        elif(times >30 and times <=40): # User rides between 31 and 40 times so those extra rides have 91.84% discount
            monthly_cost = fare*30 + (0.0816*fare)*(times - 30) + ttcfare*times
        else: # User rides more than 40 times so rides the rest for free
            monthly_cost = fare*30 + (0.0816*fare)*10 + ttcfare*times
    elif(station in toronto and localtransit):
        if (times <= 30):
            monthly_cost = fare * times + ttcfare * times
        elif (times > 30 and times <= 40):
            monthly_cost = fare * 30 + (0.0816 * fare) * (times - 30) + ttcfare * times
        else:
            monthly_cost = fare * 30 + (0.0816 * fare) * 10 + ttcfare * times
    elif(ttc == False):
        if (times <= 30):
            monthly_cost = fare * times
        elif (times > 30 and times <= 40):
            monthly_cost = fare * 30 + (0.0816 * fare)*(times - 30)
        else:
            monthly_cost = fare * 30 + (0.0816 * fare) * 10
    # Restate the train line and station user gets on, as well as how many times a month user goes to campus
    print()
    print(f"You use the {line} line and get on {station} station.")
    print(f"You go to Ryerson a total of {times} times a month.")
    print()
    # Print final result of monthly_cost rounded to 2 decimals
    print(f"You will be spending ${round(monthly_cost, 2)} a month in transportation alone to get to campus")


if __name__ == "__main__":
    # List containing all train lines available
    trains = ["Lakeshore East","Lakeshore West","Barrie","Milton","Kitchener","Richmond Hill","Stouffville"]
    # Important: List containing lists containing every possible Go Train Station
    trainstations = [["Union","Danforth","Scarborough","Eglinton","Guildwood","Rouge Hill","Pickering","Ajax","Whitby","Oshawa"],["Union", "Exhibition","Mimico","Long Branch","Port Credit","Clarkson","Oakville","Bronte","Appleby","Burlington","Aldershot","Hamilton"],["Union","Downsview Park","Rutherford","Maple","King City","Aurora","Newmarket","East Gwillimbury","Bradford","Barrie South","Allandale Waterfront"],["Union","Kipling","Dixie","Cooksville","Erindale","Streetsville","Meadowvale","Lisgar","Milton"],["Union","Bloor","Weston","Etobicoke North","Malton","Bramalea","Brampton","Mount Pleasant","Georgetown","Acton","Guelph Central","Kitchener"],["Union","Old Cummer","Langstaff","Richmond Hill","Gormley","Bloomington"],["Union","Kennedy","Agincourt","Milliken","Unionville","Centennial","Markham","Mount Joy","Stouffville","Old Elm"]]
    # Important: List containing lists containing the fare for each Go Train Station, it is in the same order as list above
    fares = [[0,2.64,2.64,3.69,3.69,4.74,5.64,6.12,6.84,7.35],[0,2.64,2.64,2.85,4.29,5.31,5.82,6.66,7.23,7.38,7.89,8.16],[0,3.69,4.89,4.89,5.61,6.09,6.69,6.84,7.38,9.15,9.48],[0,3.39,4.29,4.29,5.31,5.88,6.24,6.66,7.35],[0,2.64,3.39,3.39,5.22,5.73,6.18,6.96,7.50,8.55,9.69,11.64],[0,3.69,4.83,4.89,5.61,6.03],[0,2.64,4.62,5.43,5.55,5.64,5.64,6.03,6.84,6.84]]
    # Set containing all train stations located in Toronto to account for the 2-hour ride free on TTC
    toronto = {"Union","Danforth","Scarborough","Eglinton","Guildwood","Rouge Hill","Exhibition","Mimico","Long Branch","Downsview Park","Kipling","Bloor","Weston","Etobicoke North","Old Cummer","Langstaff","Kennedy","Agincourt"}

    calculate_trans()
