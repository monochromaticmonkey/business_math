# CustomeLifeTimeValue class references the global variables below


revenue = 20000
num_purchases = 500
num_unique_customers = 150
sum_customer_lifespans =300
period_in_months = 12
customers_begin_period = 300
customers_end_period = 280
inventory_end_period = 300
inventory_beginning_period = 250

class CustomerLifetimeValue:
    def __init__(self,revenue,num_purchases,num_unique_customers,sum_customer_lifespans,period_in_months,customers_begin_period,customers_end_period,inventory_beginning_period,inventory_end_period):
        self.revenue = revenue
        self.num_purchases = num_purchases
        self.num_unique_customers = num_unique_customers
        self.sum_customer_lifespans = sum_customer_lifespans
        self.period_in_months = period_in_months
        self.customers_begin_period = customers_begin_period
        self.customers_end_period = customers_end_period
        self.inventory_beginning_period = inventory_beginning_period
        self.inventory_end_period = inventory_end_period

        
    def average_purchase_value(self):
        #average_purchase_value_in_a_period
        return self.revenue/self.num_purchases

    def average_purchase_frequency(self):
        #average_purchase_frequency_in_a_given_period
        if self.num_purchases >  self.num_unique_customers:
            return self.num_purchases/self.num_unique_customers
        else:
            return 1

    def average_customer_lifespan(self):
        #sum_customer_lifespans expressed in months
        return self.sum_customer_lifespans/self.num_unique_customers

    def churn_rate(self):
        #churn rate is the rate at which customers drop out of your customer pool
        remaining_customers = self.customers_begin_period - self.customers_end_period
        return remaining_customers/self.customers_begin_period


    def cost_of_goods_sold(self):
        ### THIS IS NOT DONE###
        # refers to the direct cost of producting goods sold by the company. Includes matrerials and Labor cost used to create the goods and indirect expensesl like shipping and advertising.
        return self.inventory_beginning_period-self.inventory_end_period

    def gross_margin(self):
        pass
        ### THIS IS NOT DONE###
        #(revenue - cost_of_goods_sold())/revenue

    def customer_lifetime_value_wo_margin(self):
        #customer value during a year given a margin that you specify
        return self.average_purchase_value()*self.average_purchase_frequency()*self.average_customer_lifespan()

    def customer_lifetime_value_margin(self):
        #customer value during a year given a margin that you specify
        margin = .30
        return self.average_purchase_value()*self.average_purchase_frequency()*self.average_customer_lifespan()*margin
