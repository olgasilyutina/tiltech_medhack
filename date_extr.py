from natasha import DatesExtractor
import dateparser
from datetime import date
from datetime import datetime

def date_fact_to_date(date_fact):
    """
    A little helper which converts Natasha date fact object to datetime
    Arrrhhh!
    """
    
    date_str = '{} {} {}'.format(date_fact.day, date_fact.month, date_fact.year)
    dat = dateparser.parse(date_str)
    return dat


def guess_date(doc):
    """Guess what"""
    res = ""
    try:
        extractor = DatesExtractor()
        matches = extractor(doc)
        if matches:

            dates = [date_fact_to_date(match.fact) for match in matches]
            dates = [dat for dat in dates if dat < datetime.today() and dat > dateparser.parse('2010')]
            if dates:
                res = max(dates).strftime('%Y-%m-%d')
    except Exception as ex:
        print(ex)
    return res

