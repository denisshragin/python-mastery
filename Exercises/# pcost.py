# pcost.py

filename = '/Data/portfolio.dat'
filename_2 = '/Data/portfolio3.dat'
filename_3 = '/Data/portfolio2.dat'


def portfolio_cost(filename):
	total_cost = 0
	with open(filename, 'r') as f:
		for line in f:
			line_list = line.split()
			try:
				nshares = int(line_list[1])
				price = float(line_list[2])
				total_cost = total_cost + nshares*price

			# Catche errorrs
			except ValueError as e:
				print(f"Couldn't parse:", repr(line))
				print("Reason: ", e)
	return total_cost

print(portfolio_cost('/Data/portfolio.dat'))
