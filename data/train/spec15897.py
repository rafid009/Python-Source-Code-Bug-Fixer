import numpy as np 

def function(x):

	n6 = 7
	m0 = 8
	paths = []
	try:
		if n6 > 5:
			n6 = n6+4
			paths.append(1)
		else:
			m0 = m0*4
			n6 = 4*m0
			paths.append(2)
		if n6 >= 5:
			n6 = n6+x
			paths.append(3)
		else:
			m0 = n6*3
			n6 = 9-n6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n6 = x**0.5
		return n6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))