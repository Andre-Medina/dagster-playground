# code_location_2.py
import json
from dagster import StaticPartitionsDefinition

partition_ = StaticPartitionsDefinition(["A", "B","C"])  

from dagster import AssetKey, Definitions, asset
from dagster import asset, graph_asset, op


@asset
def upstream_asset():
    return 1


@op
def add_one(input_num):
    import random
    my_number = random.randint(1, 10)
    print("My number is:", my_number)
    return input_num + my_number


@op
def multiply_by_two(input_num):
    return input_num * 2


@graph_asset(partitions_def = partition_)
def middle_asset(upstream_asset):
    return multiply_by_two(add_one(upstream_asset))


@asset
def downstream_asset(middle_asset):
    return middle_asset + 7



defs = Definitions(assets=[upstream_asset,middle_asset, downstream_asset])
