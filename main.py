#!/usr/bin/env python3
import sys
import argparse
import pandas as pd
from src.scraper import get_jobs

from src.clean import merge_csv_data
from src.report import save_city_plots
from services.mail import send_email
import re
from utils.terminal import bcolors


# https://docs.python.org/3/library/argparse.html


def print_city_list():
    df = pd.read_csv('./input/world_data.csv')
    print(df['city'].unique())


def print_stats():
    df = pd.read_csv('./input/world_data.csv')
    
    print(f'{bcolors.BOLD} Job Types:\n {bcolors.ENDC}\n')
    print(f'{bcolors.OKGREEN}{df["tags"].value_counts()[:10]}{bcolors.ENDC}')
    print(f'{bcolors.BOLD} -----------------\n')
    print(f'{bcolors.BOLD}City Listings\n')
    print(f'{bcolors.OKGREEN }{df["city"].value_counts()}')

def print_city_stats(args):
    df = pd.read_csv('./input/world_data.csv')
    cities = df['city'].unique()
    city = args.city
    while city not in cities:
        city = input(
            f"Please select one of the available cities {df['city'].unique()}: ")
    filtered = df[df['city'] == city]
    table = filtered.tags.value_counts()[:20]
    print(table)
    mailto = args.mailto
    if mailto:
        save_city_plots(city)
        send_email(table, city)

def merge_file(filename):
  merge_csv_data( filename)


def scrape_url(args):
    filename = args.filename
    if not filename:
        filename = input(f"Enter filename to create with scraped data: ")
        get_jobs(args.url, filename)


def main():
    parser = argparse.ArgumentParser(description='Get data jobs info')

    parser.add_argument('--city', dest='city',
                        help='City that you want to get data jobs from')

    parser.add_argument('-l', dest='city_list', action="store_true",
                        help='List of cities there is data')

    parser.add_argument('--stats', dest='stats', action="store_true",
                        help='Get city and tag counts for all cities.')

    parser.add_argument('--scrape', dest='url',
                        help='Glasdoor url to scrape.')

    parser.add_argument('-f', dest='filename',
                        help='Filename of scraped data.')
    
    parser.add_argument('--merge', dest='merge',
                        help='File to merge.')
                        
        
    parser.add_argument('--mailto', dest='mailto', action="store_true",
                        help='Send data report by email.')
                        
    args = parser.parse_args()

    if args.city_list:
        print_city_list()
    if args.stats:
        print_stats()
    if args.city:
        print_city_stats(args)
    if args.url:
        scrape_url(args)
    if args.merge:
        merge_csv_data(args.merge)
if __name__ == "__main__":
    main()
