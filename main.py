import logging

logging.basicConfig(level=logging.DEBUG)

from compatillion.json_parser import load_file, parse_json_dict, parse_dag
from pprint import pprint

def main():
    json_dict = load_file('example_data/trf_base_clm_ibp_red_h_airline.json')
    transformation_jobs = parse_json_dict(json_dict)
    dag = parse_dag(transformation_jobs[0])
    pprint(dag)


if __name__ == '__main__':
    main()