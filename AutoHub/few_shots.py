few_shots = [{'Question': 'How many Volkswagen are available beyond the year 2010?',
  'SQLQuery': "SELECT count(*) FROM vehicles WHERE make = 'Volkswagen' AND year > 2010",
  'SQLResult': 'Result of the SQL query',
  'Answer': '9'},
 {'Question': 'How much is the total price for all quantities of Kia F-150 models?',
  'SQLQuery': "SELECT SUM(price*stock_quantity) FROM vehicles WHERE  model = 'F-150' AND make = 'Kia'",
  'SQLResult': 'Result of the SQL query',
  'Answer': '261376.00'},
 {'Question': 'If all the available quantities of Nissan cars are sold with discounts applied, how much revenue will we make?',
  'SQLQuery': "select sum(a.total_amount * ((100-COALESCE(discounts.pct_discount,0))/100)) as total_revenue from (select sum(price*stock_quantity) as total_amount, vehicle_id from vehicles where make = 'Nissan' group by vehicle_id) a left join discounts on a.vehicle_id = discounts.vehicle_id",
  'SQLResult': 'Result of the SQL query',
  'Answer': '2257611.68'},
 {'Question': 'If we have to sell all the Kia vehicles today. How much revenue will be generated without discount?',
  'SQLQuery': "SELECT SUM(price * stock_quantity) FROM vehicles WHERE make = 'Kia'",
  'SQLResult': 'Result of the SQL query',
  'Answer': '1583562.00'},
 {'Question': 'How many SUVs from Chevrolet do I actually have?',
  'SQLQuery': "SELECT sum(stock_quantity) FROM vehicles AS v where v.make = 'Chevrolet' AND v.body_style = 'SUV'",
  'SQLResult': 'Result of the SQL query',
  'Answer': '12'},
 {'Question': 'How many Chevrolet cars do I actually have?',
  'SQLQuery': "Select sum(stock_quantity) from vehicles where make= 'Chevrolet'",
  'SQLResult': 'Result of the SQL query',
  'Answer': '57'}]