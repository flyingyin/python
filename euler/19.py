from datetime import date

def getSundayCount(year):
	return len([month for month in range(1,13) if (date(year, month, 1) - date(1899, 12, 31)).days % 7 == 0])

print sum(getSundayCount(year) for year in range(1901, 2001))