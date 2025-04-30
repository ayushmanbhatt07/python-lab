
# After accidentally leaving an ice chest of fish and shrimp in your car for a week while you
# were on vacation, you’re now in the market for a new vehicle. Your insurance didn’t cover
# the loss, so you want to make sure you get a good deal on your new car.
# Define a function to calculate the monthly payment for a car loan
# Given a Series of car asking_prices and another Series of car fair_prices, determine which
# cars for sale are a good deal. In other words, identify cars whose asking price is less than
# their fair price.
# The result should be a list of integer indices corresponding to the good deals
# in asking_prices.
import pandas as pd
def find_good_deals(asking_prices, fair_prices):
    return asking_prices[asking_prices < fair_prices].index.tolist()
def calculate_monthly_payment(principal, annual_rate, years):
    monthly_rate = annual_rate / 12 / 100
    months = years * 12
    if monthly_rate == 0:  # Handle zero interest rate
        return principal / months
    return principal * (monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)

# Input details for the car loan
principal = float(input("Enter the loan amount (principal): "))
annual_rate = float(input("Enter the annual interest rate (in %): "))
years = int(input("Enter the loan term (in years): "))

# Calculate and display the monthly payment
monthly_payment = calculate_monthly_payment(principal, annual_rate, years)
print(f"Your monthly payment will be: ${monthly_payment:.2f}")