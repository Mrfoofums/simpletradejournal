from datetime import datetime


class Order:
    def __init__(self, Name, Symbol, Side, Status, Filled, Avg_Price, Placed_Time, Filled_Time):
        self.Name = Name
        self.Symbol = Symbol
        self.Side = Side
        self.Status = Status
        self.Filled = Filled
        self.Avg_Price = Avg_Price
        self.Placed_Time = self.placed_to_date(Placed_Time)
        self.Filled_Time = self.filled_to_date(Filled_Time)
        self.paired = False

    def total_purchase(self):
        if self.Avg_Price == '':
            self.Avg_Price = 0.0
        return 100 * float(self.Avg_Price) * float(self.Filled)

    def filled_to_date(self, t):
        if t == '':
            return ''
        if self.Status != 'Cancelled':
            ft = t.replace(' EST', '')
            return datetime.strptime(ft, '%m/%d/%Y %H:%M:%S')
        return ''

    def filled_as_float(self):
        return float(self.Filled)

    def avg_price_as_float(self):
        return float(self.Avg_Price)

    def placed_to_date(self, t):
        if t == '':
            return ''
        if self.Status != 'Cancelled':
            ft = t.replace(' EST', '')
            return datetime.strptime(ft, '%m/%d/%Y %H:%M:%S')
        return ''

    def print_order_details(self):
        # print(self.Symbol + ' ')
        print(f'\tQuantity: {self.Filled} Total Cost ${self.total_cost_as_float()}')

    def total_cost_as_float(self):
        if self.Side == 'Sell':
            return -100 * self.avg_price_as_float() * self.filled_as_float()
        return 100 * self.avg_price_as_float() * self.filled_as_float()


class Trade:
    def __init__(self):
        self.symbol = ''
        self.orders = []
        self.pl = 0.0

    def trade_details(self):
        print(f'{self.symbol}')
        for o in self.orders:
            o.print_order_details()
        print(f'\tTotal Profit: ${self.pl}')




