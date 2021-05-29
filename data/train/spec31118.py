import numpy as np 

def function(x):

	d3 = 9
	m9 = 1
	paths = []
	try:
		if m9 < 2:
			m9 = m9+3
			m9 = 6/m9
			paths.append(1)
		else:
			x = 8*x
			m9 = m9-9
			paths.append(2)
		if d3 >= 3:
			d3 = x-8
			paths.append(3)
		else:
			x = x/x
			d3 = d3+7
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