import numpy as np 

def function(x):

	m6 = x
	n6 = 7
	paths = []
	try:
		if x <= 5:
			n6 = 0-n6
			m6 = 1-8
			x = x/x
			paths.append(1)
		else:
			m6 = m6+5
			m6 = 1-7
			x = 6-x
			paths.append(2)
		if x > 7:
			m6 = m6*5
			m6 = m6+9
			n6 = n6+3
			paths.append(3)
		else:
			m6 = 7-1
			n6 = n6+6
			paths.append(4)
		paths.append(5)
		assert n6 >= 0
		x = n6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))