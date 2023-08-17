import argparse

parser = argparse.ArgumentParser(description = "CLI Calculator.")

subparsers = parser.add_subparsers(help="sub-command help", dest="command")

add = subparsers.add_parser("add", help="add integers")
add.add_argument("ints_to_sum", nargs=2, type=int)

sub = subparsers.add_parser("sub", help="subtract integers")
sub.add_argument("ints_to_sub", nargs=2, type=int)

mult = subparsers.add_parser("mult", help="multiply integers")
mult.add_argument("ints_to_mult", nargs=2, type=int)

div = subparsers.add_parser("div", help="divide integers")
div.add_argument("ints_to_div", nargs=2, type=int)

args = parser.parse_args()

if args.command == "add":
    our_sum = sum(args.ints_to_sum)
    print(f"the sum of values is: {our_sum}")

if args.command == "sub":
    our_diff = args.ints_to_sub[0] - args.ints_to_sub[1]
    print(f"the difference is {our_diff}")

if args.command == "mult":
    our_prod = args.ints_to_mult[0] * args.ints_to_mult[1]
    print(f"the product is {our_prod}")

if args.command == "div":

    try:
        our_quot = args.ints_to_div[0] / args.ints_to_div[1]
        print(f"the quotient is {our_quot}")
    except ZeroDivisionError:
        print(f"You can't divide by 0!")




