import argparse
import math


def calc_annuity(principal, interest, periods):
    """Calculate annuity payment."""
    i = interest / (12 * 100)  # Monthly interest rate
    annuity = principal * (i * (1 + i) ** periods) / ((1 + i) ** periods - 1)
    annuity = math.ceil(annuity)  # Ensure annuity is rounded up
    overpayment = (annuity * periods) - principal
    return annuity, math.ceil(overpayment)


def calc_loan_principal(annuity, periods, interest):
    """Calculate loan principal."""
    i = interest / (12 * 100)
    principal = annuity / ((i * (1 + i) ** periods) / ((1 + i) ** periods - 1))
    overpayment = (annuity * periods) - principal
    return principal, math.ceil(overpayment)


def calc_number_of_payments(annuity, principal, interest):
    """Calculate number of payments (months)."""
    i = interest / (12 * 100)
    months = math.log(annuity / (annuity - i * principal), 1 + i)
    months = round(months)
    overpayment = (months * annuity) - principal
    return months, math.ceil(overpayment)


def calc_differentiated_payments(principal, interest, periods):
    """Calculate and print differentiated payments with correct overpayment calculation."""
    i = interest / (12 * 100)
    total_paid = 0

    for month in range(1, periods + 1):
        diff_payment = math.ceil((principal / periods) + i * (principal - (month - 1) * (principal / periods)))
        total_paid += diff_payment
        print(f"Month {month}: payment is {diff_payment}")

    overpayment = math.ceil(total_paid - principal)
    print(f"Overpayment = {overpayment}")


def main():
    parser = argparse.ArgumentParser(description="Loan Calculator")
    parser.add_argument('--principal', type=float, help="Loan principal amount")
    parser.add_argument('--interest', type=float, help="Annual interest rate (without % sign)")
    parser.add_argument('--periods', type=int, help="Number of months")
    parser.add_argument('--payment', type=float, help="Monthly annuity payment")
    parser.add_argument('--type', type=str, help="Select either 'diff' or 'annuity'")

    args = parser.parse_args()

    # **Manually check for invalid loan type**
    if args.type not in ["annuity", "diff"]:
        print("Incorrect parameters")
        return

    # **General Parameter Validation**
    if (
        args.interest is None or args.interest < 0 or
        (args.principal is not None and args.principal < 0) or
        (args.periods is not None and args.periods < 0) or
        (args.payment is not None and args.payment < 0)
    ):
        print("Incorrect parameters")
        return

    # **Validation for "diff" payments**
    if args.type == "diff":
        if args.payment is not None or args.principal is None or args.periods is None:
            print("Incorrect parameters")
            return
        calc_differentiated_payments(args.principal, args.interest, args.periods)

    # **Validation for "annuity" payments**
    elif args.type == "annuity":
        missing_params = sum(param is None for param in [args.principal, args.payment, args.periods])
        if missing_params != 1:  # Only one parameter should be missing
            print("Incorrect parameters")
            return

        if args.payment is None:
            annuity, overpayment = calc_annuity(args.principal, args.interest, args.periods)
            print(f"Your monthly payment = {math.ceil(annuity)}!")
            print(f"Overpayment = {math.ceil(overpayment)}")

        elif args.principal is None:
            principal, overpayment = calc_loan_principal(args.payment, args.periods, args.interest)
            print(f"Your loan principal = {math.ceil(principal)}!")
            print(f"Overpayment = {overpayment}")

        elif args.periods is None:
            months, overpayment = calc_number_of_payments(args.payment, args.principal, args.interest)
            years = months // 12
            remaining_months = months % 12

            if years > 0:
                print(f"It will take {years} years and {remaining_months} months to repay this loan!")
            else:
                print(f"It will take {remaining_months} months to repay this loan!")
            print(f"Overpayment = {overpayment}")


if __name__ == "__main__":
    main()
