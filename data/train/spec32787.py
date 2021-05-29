import numpy as np 

def function(x):

	m7 = 8
	d3 = x
	paths = []
	try:
		if x < 1:
			m7 = d3*x
			x = x-2
			paths.append(1)
		else:
			m7 = 9/x
			m7 = x/m7
			paths.append(2)
		if d3 <= 6:
			d3 = d3/8
			x = 3+2
			paths.append(3)
		else:
			x = 8/m7
			paths.append(4)
		paths.append(5)
		assert d3 >= 0
		m7 = d3**0.5
		return m7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))