with base as (
  select *,
    case
      when customer_id is not null 
        then row_number() over (partition by customer_id order by visitor_id ASC) 
      else 1
      end as id_dup
  from `analytics-engineers-club.web_tracking.pageviews`
)

, dupes as (
  select customer_id, visitor_id
  from base 
  where id_dup = 1
)

, dedup as (select 
  id,
  case
    when id_dup = 1 then a.visitor_id
    else b.visitor_id
  end as visitor_id,
  device_type,
  timestamp,
  page,
  customer_id
from base a
left join dupes b using(customer_id)
)

select *
from dedup
