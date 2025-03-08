#Ben Krehbiel
#3/7/2025
#rainy days


def get_rain():
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]

    rainfall = []


    for month in months:
        while True:
            try:
                amount = float(input(f"Enter the total rainfall for {month}: "))
                if amount < 0:
                    print("This isn't the desert, enter a positive number.")
                else:
                    rainfall.append(amount)
                    break
            except ValueError:
                print("Invalid input, try again.")


    total_rainfall = sum(rainfall)
    average_rainfall = total_rainfall / 12
    max_rainfall = max(rainfall)
    min_rainfall = min(rainfall)


    max_month = months[rainfall.index(max_rainfall)]
    min_month = months[rainfall.index(min_rainfall)]

    print("Rainfall Statistics:\n"
         f"Total Rainfall: {total_rainfall:.2f} inches\n"
         f"Average Monthly Rainfall: {average_rainfall:.2f} inches\n"
         f"Highest Rainfall: {max_rainfall:.2f} inches in {max_month}\n"
         f"Lowest Rainfall: {min_rainfall:.2f} inches in {min_month}\n")

get_rain()
