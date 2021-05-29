import numpy as np 

def function(x):

	n7 = x
	m6 = 4
	paths = []
	try:
		if x <= 2:
			m6 = n7+3
			x = x*3
			paths.append(1)
		else:
			m6 = m6+4
			paths.append(2)
		if m6 > 4:
			m6 = x-5
			paths.append(3)
		else:
			n7 = 2*n7
			x = x*x
			paths.append(4)
		paths.append(5)
		assert m6 >= 0
		x = m6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))