import csv
import re #regularExpressions
def process_csv(input_file, output_file, categoryDictionary):
  with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
    reader = csv.reader(f_in)
    writer = csv.writer(f_out)

    #take care of the header
    writer.writerow(next(reader))  

    for row in reader:
      expense = row[0]  
      for expenseKey, category in categoryDictionary.items():
        if re.search(rf"\b{expenseKey}\b", expense, flags=re.IGNORECASE):
          row[3] = category
          break  
      writer.writerow(row)

# Example usage
input_file = "./data.csv"
output_file = "./result.csv"
categoryDictionary = {"MANAGER": "OFFICER COMPENSATION", 
                      "PAGO NICOLE ": "EMPLOYEE PAY",                     
                      "PAGO MANAGER. ": "OFFICER COMPENSATION", 
                      "GASOLINA CHEO Y JOSE": "FUEL", 
                      "TOLL": "PARKING AND TOLLS", 
                      "CAMION ROBADO ": "EQUIPMENT LEASE O RENTAL", 
                      "ADP FEES": "PERMIT AND FEES", 
                      "WORKER COMP": "INSURANCE", 
                      "ADP TAX": "TAXES AND LICENSES", 
                      "SUNPASS": "PARKING AND TOLLS", 
                      "UBER": "TRAVEL", 
                      "ENTERPRISE HOLDING": "REPAIR AND MAITENANCE", 
                      "AUTOZONE": "REPAIR AND MAITENANCE", 
                      "RYDER FEES": "EQUIPMENT LEASE O RENTAL", 
                      "ADP 401K": "OFFICER COMPENSATION", 
                      "LYFT": "TRAVEL", 
                      "THE SIMPLEX GROUP": "PERMIT AND FEES", 
                      "DOORDASH": "MEALS", 
                      "GASOLINA JJJ": "FUEL", 
                      "ATT": "CELLPHONE", 
                      "PAGO CHEO ": "OFFICER COMPENSATION", 
                      "UBER EATS ": "MEALS", 
                      "WILLIAM MECANICO  ": "REPAIR AND MAITENANCE", 
                      "LIBERTY MUTUAL":"INSURANCE",
                      "LIBERTY MUTUAL":"INSURANCE",
                      "PAGO JOSE":"OFFICER COMPENSATION",
                      "PAGO CHEO":"OFFICER COMPENSATION",
                      "PAGO NICOLE":"EMPLOYEE PAY",
                      "NATIONWIDE":"INSURANCE",
                      "MECANICO":"REPAIR AND MAINTENANCE",
                      "EXPEDIA":"TRAVEL",
                      "EXPEDIA":"TRAVEL",
                      "EXPEDIA":"TRAVEL",
                      "EXPEDIA":"TRAVEL",
                      "EXPEDIA":"TRAVEL",
                      "EXPEDIA":"TRAVEL",
                      "EXPEDIA":"TRAVEL",
                      "AIRBNB": "TRAVEL"}

process_csv(input_file, output_file, categoryDictionary)
print(f"Processing complete, results saved to {output_file}")
