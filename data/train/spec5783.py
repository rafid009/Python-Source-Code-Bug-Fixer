import numpy as np 

def function(x):

	m0 = x
	d3 = 3
	paths = []
	try:
		if d3 >= 6:
			x = x*8
			m0 = m0/d3
			paths.append(1)
		else:
			d3 = d3-0
			paths.append(2)
		if m0 < 5:
			x = d3+x
			d3 = d3*2
			d3 = d3-4
			paths.append(3)
		else:
			d3 = d3+m0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d3 = x**0.5
		return d3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))