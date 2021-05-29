import numpy as np 

def function(x):

	n2 = 3
	m2 = x
	paths = []
	try:
		if x >= 9:
			x = m2*5
			m2 = m2*x
			paths.append(1)
		else:
			x = m2-5
			paths.append(2)
		if m2 > 3:
			n2 = x+2
			paths.append(3)
		else:
			x = 5*n2
			x = 3-m2
			x = 1/m2
			paths.append(4)
		paths.append(5)
		assert m2 >= 0
		x = m2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))