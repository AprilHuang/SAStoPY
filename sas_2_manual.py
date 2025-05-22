
import saspy
import pandas as pd
from datetime import datetime

# Configure your SAS connection (see saspy docs for details)
sas = saspy.SASsession(cfgname='your_config')

# Read the SAS dataset from the remote library
electric = sas.sasdata('electric', libref='libref').to_df()
fashion = sas.sasdata('fashion', libref='libref').to_df()

## SET statement to concatenate two datasets having same variables
ele_fsn_concat = pd.concat([electric, fashion], ignore_index=True)


## SET statement to concatenate datasets in which one is having more variable than other
admindept = pd.DataFrame({
    'empid': [1, 3, 6],
    'name': ['Rick', 'Mike', 'Tusar'],
    'salary': [623.3, 611.5, 578.6],
    'DOJ': [datetime.strptime(d, '%d%b%Y') for d in ['02APR2001', '21OCT2000', '01MAR2009']]
})
financedept = pd.DataFrame({
    'empid': [2, 4, 7],
    'name': ['Andy', 'Rusell', 'John'],
    'salary': [567.2, 683.2, 594.5]
})


### this won't work
admin_finance_concat = pd.concat([admindept, financedept], ignore_index=True)

### this will work
admindept_appended = pd.concat([admindept, financedept], ignore_index=True, sort=False)
financedept_appended = pd.concat([financedept, admindept], ignore_index=True, sort=False)

### sort first and then merge
admindept_appended = admindept_appended.sort_values(by='custID')
financedept_appended = financedept_appended.sort_values(by='custID')
interleavedata = pd.merge(admindept_appended, financedept_appended, on='id')

## One-to-One Reading
customer = pd.DataFrame({
    'orderid': [1, 2, 3, 4, 5],
    'sales': [5000, 6000, 4000, 8000, 7000],
    'product': ['Camera', 'TV', 'Fridge', 'Laptop', 'Desktop']
})

sales = pd.DataFrame({
    'orderid': [1, 2, 3, 4, 5, 6],
    'customername': ['Mike', 'Rusell', 'Adam', 'Gary', 'Steve', 'Craig'],
    'pincode': [560035, 560045, 560078, 560075, 560076, 560035]
})
onetoonereadset = pd.concat([customer, sales], axis=1)

import pandas as pd

# Customer DataFrame (from earlier in your SAS code)
customer = pd.DataFrame({
    'orderid': [1, 2, 3, 4, 5],
    'sales': [5000, 6000, 4000, 8000, 7000],
    'product': ['Camera', 'TV', 'Fridge', 'Laptop', 'Desktop']
})

# Sales DataFrame (from your new datalines)
sales = pd.DataFrame({
    'orderid': [1, 2, 3, 6, 7, 8],
    'customername': ['Mike', 'Rusell', 'Adam', 'Gary', 'Steve', 'Craig'],
    'pincode': [560035, 560045, 560078, 560075, 560076, 560035]
})

one2one_concat = pd.concat([customer, sales], axis=1)
one2oone_mergeset = pd.merge(sales, customer, on='orderid', how='outer')
onet2one_mergeset_rev = pd.merge(customer, sales, on='orderid', how='outer')

