

# The CLV class can call fuctions necessary for calculationg CLV and return CLV (w/h or w/h out Margin)
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
        #sum_customer_lifespans expressed in months - generally 12 or 24 months
        ## your intial data should be pulled within a specific period as to avoid inaccurate values
        return self.sum_customer_lifespans/self.num_unique_customers

    def churn_rate(self):
        #churn rate is the rate at which customers drop out of your customer pool
        ## Not Actively Used in the following Script but Useful for Understand Your Customer Retention
        remaining_customers = self.customers_begin_period - self.customers_end_period
        return remaining_customers/self.customers_begin_period


    def cost_of_goods_sold(self):
        ## THIS IS NOT DONE 
        ### Comming Soon to a Script Near You
        # refers to the direct cost of producting goods sold by the company. Includes matrerials and Labor cost used to create the goods and indirect expensesl like shipping and advertising.
        return self.inventory_beginning_period-self.inventory_end_period

    def gross_margin(self):
        pass
        ### THIS IS NOT DONE ###
        #(revenue - cost_of_goods_sold())/revenue

    def customer_lifetime_value_wo_margin(self):
        #customer value during a year given a margin that you specify
        return self.average_purchase_value()*self.average_purchase_frequency()*self.average_customer_lifespan()

    def customer_lifetime_value_margin(self):
        #customer value during a year given a margin that you specify
        margin = .30
        return self.average_purchase_value()*self.average_purchase_frequency()*self.average_customer_lifespan()*margin
