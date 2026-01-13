# -*- coding: utf-8 -*-
"""
Created on Wed Dec 17 22:50:23 2025

@author: Allie
"""

from . import fileparse
from .portfolio import Portfolio
from . import tableformat

def read_portfolio(filename, **opts):

    with open(filename) as lines:
        return Portfolio.from_csv(lines, **opts)

def read_prices(filename, **opts):

    with open(filename) as lines:
        return dict(fileparse.parse_csv(lines, types=[str,float], has_headers=False, **opts))

def make_report(portfolio, prices):

    rows = []
    for s in portfolio:
        current_price = prices[s.name]
        change = current_price - s.price
        summary = (s.name, s.shares, current_price, change)
        rows.append(summary)
    return rows

def print_report(reportdata, formatter):
 
    formatter.headings(['Name','Shares','Price','Change'])
    for name, shares, price, change in reportdata:
        rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
        formatter.row(rowdata)

def portfolio_report(portfoliofile, pricefile, fmt='txt'):

    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    report = make_report(portfolio, prices)

    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)

def main(args):
    if len(args) != 4:
        raise SystemExit('Usage: %s portfile pricefile format' % args[0])
    portfolio_report(args[1], args[2], args[3])

if __name__ == '__main__':
    import sys
    main(sys.argv)