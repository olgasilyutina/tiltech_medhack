from natasha import DatesExtractor
import dateparser

def date_fact_to_date(date_fact):
    """
    A little helper which converts Natasha date fact object to datetime
    Arrrhhh!
    """
    
    date_str = '{} {} {}'.format(date_fact.day, date_fact.month, date_fact.year)
    date = dateparser.parse(date_str)
    return date


def guess_date(doc):
    """Guess what"""
    
    extractor = DatesExtractor()
    matches = extractor(doc)
    dates = [date_fact_to_date(match.fact) for match in matches]
    return max(dates).strftime('%Y-%m-%d')

