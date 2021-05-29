import numpy as np 

def function(x):

	m0 = x
	v1 = 2
	paths = []
	try:
		if m0 >= 3:
			x = 6-x
			paths.append(1)
		else:
			m0 = m0+1
			paths.append(2)
		if x >= 2:
			v1 = v1*v1
			x = x+6
			paths.append(3)
		else:
			v1 = v1-6
			x = 9*x
			paths.append(4)
		paths.append(5)
		assert m0 >= 0
		v1 = m0**0.5
		return v1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))