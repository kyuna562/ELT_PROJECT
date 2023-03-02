with 
m as (
    select
        *
    from
        {{ref('src_markets')}}
),
c as (
    select
        *
    from
        {{ref('src_contracts')}}
)
select
    m.predictit_name,
    m.predictit_short_name,
    m.predictit_url,
    c.id,
    c.PREDICTIT_CONTRACT_ID,
    c.IMAGE,
    c.END_DATE,
    c.CONTRACT_NAME,
    c.CONTRACT_STATUS_NAME,
    c.CONTRACT_SHORT_NAME,
    c.LAST_TRADE_PRICE,
    c.BEST_BUY_YES_COST,
    c.BEST_BUY_NO_COST,
    c.BEST_SELL_YES_COST,
    c.BEST_SELL_NO_COST,
    c.LAST_CLOSE_PRICE,
    c.DATEID
FROM c
left join m on (m.id = c.id)



