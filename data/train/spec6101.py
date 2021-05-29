import numpy as np 

def function(x):

	n9 = x
	m1 = 8
	paths = []
	try:
		if n9 > 5:
			n9 = n9+3
			x = 2+x
			n9 = n9-3
			paths.append(1)
		else:
			n9 = 0*7
			paths.append(2)
		if n9 >= 8:
			x = x*m1
			x = x*4
			n9 = 5/7
			paths.append(3)
		else:
			n9 = n9-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m1 = x**0.5
		return m1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))