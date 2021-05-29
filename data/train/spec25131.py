import numpy as np 

def function(x):

	m5 = 9
	d9 = 0
	paths = []
	try:
		if d9 >= 3:
			d9 = d9*6
			d9 = m5-7
			paths.append(1)
		else:
			x = x*3
			paths.append(2)
		if d9 > 2:
			d9 = d9/x
			paths.append(3)
		else:
			m5 = 9+0
			m5 = 7-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m5 = x**0.5
		return m5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))