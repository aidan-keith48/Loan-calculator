# Loan Calculator

## Overview
This Loan Calculator is a command-line tool that calculates loan-related values based on user input. It supports **annuity payments** and **differentiated payments**.

## Features
- Calculate monthly annuity payments.
- Determine the number of months required to repay a loan.
- Compute loan principal based on monthly payment.
- Calculate differentiated payments for loans.
- Displays overpayment details.
- Validates input parameters and handles errors gracefully.

## Usage
Run the script using Python and provide the necessary arguments.

### **Command Structure:**
```
python creditcalc.py --type=<annuity|diff> --principal=<amount> --interest=<rate> --periods=<months> --payment=<amount>
```

### **Parameters:**
| Parameter       | Required | Description |
|---------------|-----------|-------------------------------------------------------------|
| `--type`     | Yes       | Loan type: "annuity" or "diff" (differentiated payments)  |
| `--principal` | Sometimes | Loan principal amount. Required for some calculations.     |
| `--interest`  | Yes       | Annual interest rate (without the % sign).               |
| `--periods`   | Sometimes | Number of months to repay the loan. Required for some calculations. |
| `--payment`   | Sometimes | Monthly annuity payment. Required when calculating principal or periods. |

**Important Notes:**
- `--interest` is **mandatory** for all calculations.
- For `diff` type, `--payment` **should not be provided**.
- Only **one parameter** can be missing for annuity-type calculations.
- If invalid parameters are passed, the program prints `Incorrect parameters`.

## Examples

### **Calculate Annuity Payment:**
```
python creditcalc.py --type=annuity --principal=1000000 --interest=10 --periods=60
```
**Output:**
```
Your monthly payment = 21247!
Overpayment = 274820
```

### **Calculate Loan Principal:**
```
python creditcalc.py --type=annuity --payment=8722 --periods=120 --interest=5.6
```

### **Calculate Number of Payments:**
```
python creditcalc.py --type=annuity --principal=500000 --payment=23000 --interest=7.8
```

### **Calculate Differentiated Payments:**
```
python creditcalc.py --type=diff --principal=1000000 --interest=10 --periods=8
```

**Output:**
```
Month 1: payment is 105000
Month 2: payment is 103750
...
Overpayment = 25000
```

## Error Handling
If the input parameters are incorrect, the program will print:
```
Incorrect parameters
```

## Requirements
- Python 3.x

## Running the Script
Ensure you have Python installed, then run:
```
python creditcalc.py <arguments>
```

## License
This project is open-source and available for modification.

