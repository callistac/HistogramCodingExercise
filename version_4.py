import matplotlib.pyplot as plt
import argparse
import csv


def load_data(input_data):
    '''
    Reads in the input CSV file and stores data in list of tuple format: [('cheese', 2), ('sausage', 7) ...]
    '''
    pizza_orders = []
    with open(input_data, newline='') as input_csv:
        input_csv = csv.reader(input_csv, quoting=csv.QUOTE_NONNUMERIC) # converts all non-quoted fields to float type
        next(input_csv, None)  # skip the headers of the CSV file
        for row in input_csv:
            pizza_orders.append(tuple(row))
    return pizza_orders

def aggregate_orders(pizza_orders):
    '''
    Aggregates the counts of all the orders with the same topping to obtain a histogram of total counts per topping.
    '''
    hist = {}
    for pizza_type, num_orders in pizza_orders:
        if pizza_type in hist.keys():
            hist[pizza_type] += num_orders
        else:
            hist[pizza_type] = num_orders
    return hist

def print_orders(hist):
    '''
    Prints the aggregated pizza orders to the command line.
    '''
    print("Order Breakdown")
    print("---------------")
    for pizza, num_order in hist.items():
        print("{}: {}".format(pizza, int(num_order)))
    return

def generate_visualization(hist):
    '''
    Generates a visualization displaying the histogram of the aggregated pizza orders.
    '''
    plt.figure(figsize=(8, 6))
    plt.bar(list(hist.keys()), hist.values(), color='gold', hatch='O')
    plt.title("Daily Pizza Orders", fontsize=16)
    plt.xlabel("Pizza Type", fontsize=14); plt.ylabel("Total Orders", fontsize=14)
    return plt

def show_hist(plt):
    '''
    Displays histogram on the user's screen.
    '''
    plt.show()
    return

def save_hist(plt, output_filename):
    '''
    Saves histogram figure to user's computer at the specified output_filename path.
    '''
    plt.savefig(output_filename)
    return

def main(pizza_orders_csv, save_fig=True, show_plot=True, filename="orders.png"):
    pizza_orders = load_data(pizza_orders_csv)
    agg_orders = aggregate_orders(pizza_orders)
    print_orders(agg_orders)
    plt = generate_visualization(agg_orders)
    if save_fig: save_hist(plt, filename)
    if show_plot: show_hist(plt)
    return

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Aggregate pizza orders')
    parser.add_argument('-p', '--pizza_data', help='Please enter a path to where the data is stored', required=True)
    parser.add_argument('-d', '--display', help='Display the output histogram? Type True or False', required=False, default=True)
    parser.add_argument('-s', '--save', help='Save the output histogram? Type True or False', required=False, default=True)
    parser.add_argument('-f', '--filename', help='Select a filename your output histogram will be saved as.', required=False, default="orders.png")

    args = parser.parse_args()
    display =  False if args.display == "False" else True
    save = False if args.save == "False" else True
    main(args.pizza_data, save, display, args.filename)