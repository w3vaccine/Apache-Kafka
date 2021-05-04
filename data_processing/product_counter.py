import faust
import sys
sys.path.insert(1, '/Users/zharas/Desktop/ttask/shared_functions')

from funtion_a import Products

app = faust.App('hit_counter',broker="kafka://localhost:29092")

class productCount(faust.Record,validation=True):
    products: int
    productId: int


hit_topic = app.topic("hit_count",value_type=productCount)
extra_topic = app.topic('extra_topic', internal=True, value_type=productCount)
count_table = app.Table("major-count" ,key_type=str, value_type=int, partitions=1, default=int)


@app.agent(hit_topic)
async def count_hits(counts):
    async for count in counts:
        print(f"Data recieved is {count}")
        if Products.function(count.products):
            await extra_topic.send(value=count)

@app.agent(extra_topic)
async def show_count(counts):
    async for count in counts:
        print(f"Count in extra topic is {count}")
 