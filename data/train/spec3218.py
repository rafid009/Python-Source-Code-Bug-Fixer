import numpy as np 

def function(x):

	m3 = 2
	n1 = 4
	x = x
	paths = []
	try:
		if n1 < 3:
			m3 = 9+6
			m3 = 1*6
			n1 = n1*n1
			paths.append(1)
		else:
			n1 = 1-n1
			x = x/5
			x = x*5
			paths.append(2)
		if m3 < 7:
			x = 1-x
			paths.append(3)
		else:
			x = 1/x
			m3 = 1*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n1 = x**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))