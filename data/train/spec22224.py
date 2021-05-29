import numpy as np 

def function(x):

	m2 = x
	n6 = x
	x = 7
	paths = []
	try:
		if n6 >= 4:
			n6 = 8/n6
			paths.append(1)
		else:
			n6 = n6-5
			paths.append(2)
		if m2 >= 4:
			m2 = m2+2
			paths.append(3)
		else:
			n6 = 2/n6
			x = x-x
			x = x+0
			paths.append(4)
		paths.append(5)
		assert n6 >= 0
		n6 = n6**0.5
		return n6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))