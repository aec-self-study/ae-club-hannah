with base as (
select 
  orders.created_at,
  products.category,
  product_prices.price
from `analytics-engineers-club.coffee_shop.order_items` as order_items
left join `analytics-engineers-club.coffee_shop.orders` as orders 
  on order_items.order_id = orders.id
left join `analytics-engineers-club.coffee_shop.products` as products 
  on order_items.product_id = products.id
left join `analytics-engineers-club.coffee_shop.product_prices` as product_prices
  on order_items.product_id = product_prices.product_id
  and orders.created_at between product_prices.created_at and product_prices.ended_at
)

, categories as (select
date(date_trunc(created_at,week)) as start_of_week,
category,
sum(price) as revenue
from base
group by 1,2
order by 1,2
)

select 
  start_of_week,
  date_add(start_of_week,interval 6 day) as end_of_week,
  case
    when category = 'coffee beans' then 'coffee_beans'
    when category = 'merch' then 'merch'
    when category = 'brewing supplies' then 'brewing_supplies'
    else null
  end as category,
  revenue
from categories