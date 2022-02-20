import csv
from order import Order
from order import Trade


# Press the green button in the gutter to run the script.
def symbol_p_l(orders: list):
    pl = 0.0
    for order in orders:
        pl += order.total_cost_as_float()
    return pl


def days_p_l(trades: list):
    pl = 0.0
    for t in trades:
        pl += t.pl
    return pl


if __name__ == '__main__':
    with open('orders.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        Orders = []
        for line in csv_reader:
            order = Order(line['Name'], line['Symbol'], line['Side'], line['Status'], line['Filled'], line['Avg Price'],
                          line['Placed Time'], line['Filled Time'])
            Orders.append(order)

        Orders = list(filter(lambda o: o.Status != 'Cancelled', Orders))
        Orders.sort(key=lambda l: l.Filled_Time)

        # Find each unique symbol and put in in a set
        uniqueSymbols = set()
        for o in Orders:
            uniqueSymbols.add(o.Symbol)

        trades = []
        for symbol in uniqueSymbols:
            ordersWithSymbol = list(filter(lambda o: o.Symbol == symbol, Orders))

            trade = Trade()
            trade.symbol = symbol
            trade.orders = ordersWithSymbol
            trade.pl = symbol_p_l(ordersWithSymbol)
            trades.append(trade)

        total_pl = days_p_l(trades)
        print(f'Total Profit: {total_pl}')

        with open('profit-loss.csv', 'w') as new_file:
            fieldnames = ['Symbol', 'Day Notes', 'Time Filled', 'Quantity Filled', 'Avg Price', 'Market Value', 'Profit',
                          'Day Profit', 'Order Notes']

            csv_writer = csv.writer(new_file)

            csv_writer.writerow(fieldnames)
            for t in trades:
                #Write the symbol

                firstrow = [t.symbol]
                csv_writer.writerow(firstrow)
                for o in t.orders:
                    row = ['', '', o.Filled_Time.strftime("%m/%d/%Y, %H:%M:%S"), str(o.filled_as_float()), str(o.avg_price_as_float()), str(o.total_cost_as_float())]
                    csv_writer.writerow(row)

                #after each order write the trade summarty row
                summary = ['', '', '', '', '', '', t.pl]
                csv_writer.writerow(summary)
            csv_writer.writerow(['', '', '', '', '', '', '', days_p_l(trades)])