with STG_PREDICTIT_MARKETS as (
    select 
        *
    from RAW.PUBLIC.STG_PREDICTIT_MARKETS
)
select
    id,
    predictit_name,
    predictit_short_name,
    predictit_url
from 
    RAW.PUBLIC.STG_PREDICTIT_MARKETS