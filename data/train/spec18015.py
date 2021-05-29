import numpy as np 

def function(x):

	m5 = 0
	n5 = 5
	x = x
	paths = []
	try:
		if m5 > 0:
			m5 = 1-m5
			paths.append(1)
		else:
			m5 = 2*n5
			paths.append(2)
		if n5 >= 2:
			m5 = m5*m5
			n5 = n5-x
			paths.append(3)
		else:
			n5 = 0/x
			paths.append(4)
		paths.append(5)
		assert n5 >= 0
		n5 = n5**0.5
		return n5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))