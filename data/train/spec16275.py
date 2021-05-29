import numpy as np 

def function(x):

	d3 = 9
	m8 = x
	paths = []
	try:
		if x >= 7:
			x = 1+3
			d3 = 6/d3
			m8 = m8-8
			paths.append(1)
		else:
			x = x-0
			m8 = m8/m8
			paths.append(2)
		if x <= 4:
			d3 = d3-9
			d3 = 0+d3
			paths.append(3)
		else:
			d3 = d3-8
			m8 = 6+m8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))