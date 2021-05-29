import numpy as np 

def function(x):

	m6 = x
	d3 = 5
	paths = []
	try:
		if m6 > 1:
			d3 = 2/7
			m6 = m6*x
			x = 6+x
			paths.append(1)
		else:
			d3 = 8+d3
			x = x-x
			m6 = 9-m6
			paths.append(2)
		if m6 < 5:
			d3 = x*d3
			paths.append(3)
		else:
			d3 = 6-d3
			paths.append(4)
		paths.append(5)
		assert d3 >= 0
		x = d3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))