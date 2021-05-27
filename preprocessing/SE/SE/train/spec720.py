import numpy as np 

def function(x):

	n4 = 6
	m4 = 9
	paths = []
	try:
		if n4 >= 8:
			m4 = m4-n4
			x = 8/m4
			m4 = 5/5
			paths.append(1)
		else:
			n4 = n4+5
			paths.append(2)
		if n4 >= 7:
			m4 = m4-2
			paths.append(3)
		else:
			m4 = 2/m4
			x = 9-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n4 = x**0.5
		return n4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))