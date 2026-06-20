# Scenario 1:  Reconcille data between Source ( oracle) and Target(mysql)
import pandas as pd
from sqlalchemy import create_engine
import cx_Oracle
oracle_conn = create_engine("oracle+cx_oracle://system:admin@localhost:1521/xe")
mysql_conn = create_engine("mysql+pymysql://root:Admin%40143@localhost:3308/apr_weekend")


def compare_data_between_source_and_target(oracle_conn,mysql_conn):
    query_source = """select * from products"""
    df_source = pd.read_sql(query_source,oracle_conn)

    query_target = """select * from product_output"""
    df_target = pd.read_sql(query_target,mysql_conn)

    # check if all the product_ids are available in target

    df_ans = df_source[~df_source['product_id'].isin(df_target['product_id'])]

    extra_count = df_ans['product_id'].count()
    if extra_count == 0:
        print("Test Passed")
    else:
        df_ans.to_csv("data/extra_in_source.csv", index=False)
        print("Test Failed")
def compare_data_between_target_and_source(oracle_conn,mysql_conn):
    query_source = """select * from products"""
    df_source = pd.read_sql(query_source,oracle_conn)

    query_target = """select * from product_output"""
    df_target = pd.read_sql(query_target,mysql_conn)

    # check if all the product_ids are available in target

    df_ans = df_target[~df_target['product_id'].isin(df_source['product_id'])]

    extra_count = df_ans['product_id'].count()
    if extra_count == 0:
        print("Test Passed")
    else:
        df_ans.to_csv("data/extra_in_target.csv", index=False)
        print("Test Failed")

compare_data_between_source_and_target(oracle_conn,mysql_conn)
compare_data_between_target_and_source(oracle_conn,mysql_conn)


