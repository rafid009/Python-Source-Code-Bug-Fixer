import numpy as np 

def function(x):

	d3 = x
	m4 = 9
	paths = []
	try:
		if m4 <= 7:
			x = x*5
			d3 = d3/5
			x = 5+x
			paths.append(1)
		else:
			m4 = m4-d3
			d3 = 6*d3
			paths.append(2)
		if d3 > 1:
			x = d3-x
			x = 6-x
			paths.append(3)
		else:
			d3 = d3-9
			m4 = 9-m4
			d3 = d3+x
			paths.append(4)
		paths.append(5)
		assert m4 >= 0
		x = m4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))