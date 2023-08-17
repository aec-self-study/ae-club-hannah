{% set product_categories = ["coffee_beans", "merch", "brewing_supplies"] %}
select
  date_trunc(start_of_week, month) as date_month,
  {% for product_category in product_categories %}
  sum(case when category = '{{product_category}}' then revenue end) as {{product_category}}_amount
  {% if not loop.last %},{% endif %}
  {% endfor %}
  --sum(case when category = 'coffee beans' then revenue end) as coffee_beans_amount,
  --sum(case when category = 'merch' then revenue end) as merch_amount,
  --sum(case when category = 'brewing supplies' then revenue end) as brewing_supplies_amount
-- you may have to `ref` a different model here, depending on what you've built previously
from {{ ref('weekly_sales') }}
group by 1