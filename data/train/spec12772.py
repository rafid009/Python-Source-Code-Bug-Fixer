import numpy as np 

def function(x):

	n4 = 7
	m1 = x
	paths = []
	try:
		if n4 >= 7:
			m1 = m1*1
			paths.append(1)
		else:
			m1 = m1-m1
			x = x-n4
			paths.append(2)
		if n4 < 9:
			n4 = 3*n4
			n4 = 9/n4
			n4 = n4-0
			paths.append(3)
		else:
			m1 = m1+n4
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