import csv
from order import Order
from order import Trade

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open('orders.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        Orders = []
        for line in csv_reader:
            order = Order(line['Name'], line['Symbol'], line['Side'], line['Status'], line['Filled'], line['Avg Price'], line['Placed Time'], line['Filled Time'])
            Orders.append(order)

        Orders = list(filter(lambda o: o.Status != 'Cancelled', Orders))
        Orders.sort(key=lambda l: l.Filled_Time)
        #Find each unique symbol and put in in a set
        uniqueSymbols = set()
        for o in Orders:
            uniqueSymbols.add(o.Symbol)

        for symbol in uniqueSymbols:
            ordersWithSymbol = list(filter(lambda o: o.Symbol == symbol, Orders))

            for order in ordersWithSymbol:
                #Print all the orders for each symbol
                order.print_order_details()


        trades = []

        # for order in Orders:
        #     if order.Side == 'Buy':
        #         # Find an open order
        #         trade = Trade()
        #         trade.openOrder = Order('', '', '', '', '', '', '', '')
        #         trade.closeOrder = Order('', '', '', '', '', '', '', '')
        #         allOrders = filter(lambda l: l.Symbol == order.Symbol, Orders)
        #         for i in allOrders:
        #             if i.Side == 'Buy':
        #                 trade.openOrder = i
        #
        #             if i.Side == 'Sell':
        #                 trade.closeOrder = i
        #
        #         trades.append(trade)
        #
        # for trade in trades:
        #     print(trade.openOrder.Avg_Price)
        #     if trade.closeOrder:
        #         print(trade.closeOrder.Avg_Price)


        # print(Trades)


        # with open('profit-loss.csv', 'w') as new_file:
        #     fieldnames = ['Symbol', 'Side', 'Avg Price', 'Placed Time', 'Filled', 'Time-in-Force', 'Filled Time', 'Status', 'Total Qty', 'Price', 'Name']

            # csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
            #
            # csv_writer.writeheader()

            # for line in csv_reader:
            #     if '@' not in line['Price']:
            #         print(line['Name']+' Total Price=' + str(100 * float(line['Price'])*float(line['Total Qty'])))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/




#General algo should be
# 1. Chronologically sort all trades for the day, they come this way already so we can actually save time by just first grouping them
# 2. For v1 I think I just want to organize by symbol organize those by time and then find hte P&L for that symbol on the day. I can then construct a total day P&L from all of the trades

def days_p_l(orders):
    return ''