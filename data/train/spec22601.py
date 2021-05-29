import numpy as np 

def function(x):

	m5 = x
	n0 = x
	paths = []
	try:
		if x <= 8:
			m5 = m5+7
			paths.append(1)
		else:
			m5 = 0*x
			paths.append(2)
		if n0 >= 8:
			m5 = 1+6
			n0 = n0*4
			paths.append(3)
		else:
			x = m5-0
			m5 = x-m5
			m5 = n0-m5
			paths.append(4)
		paths.append(5)
		assert n0 >= 0
		n0 = n0**0.5
		return n0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))