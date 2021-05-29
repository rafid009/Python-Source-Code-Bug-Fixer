import numpy as np 

def function(x):

	m1 = x
	n7 = x
	paths = []
	try:
		if m1 >= 2:
			m1 = m1-x
			paths.append(1)
		else:
			n7 = n7-1
			n7 = n7/x
			paths.append(2)
		if m1 > 1:
			x = 5-3
			paths.append(3)
		else:
			x = x*7
			x = x-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n7 = x**0.5
		return n7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))