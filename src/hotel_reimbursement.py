def calculate_cost_difference(original_reservation_total, hotel_nights_cost):
  # Calculate 20% of the original reservation total
  max_difference = original_reservation_total * 0.20

  # Calculate the difference between the original reservation total and the hotel nights cost
  cost_difference = hotel_nights_cost - original_reservation_total

  if cost_difference <= 0:
      print("No reimbursement needed.")
  elif cost_difference > max_difference:
      print("The maximum reimbursement amount should be: ${:.2f}. If you think the amount is not appropriate, please reach out to a TL for second oppinion.".format(max_difference))
  else:
      print("You can reimburse the entire difference!")

def main():
  # Ask for the original reservation total
  original_reservation_total = float(input("Enter the total amount paid for the original reservation: $"))

  # Ask for the cost of the nights at the hotel
  hotel_nights_cost = float(input("Enter the total amount paid for the nights at the hotel: $"))

  # Calculate the cost difference
  calculate_cost_difference(original_reservation_total, hotel_nights_cost)

if __name__ == "__main__":
  main()

