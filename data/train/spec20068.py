import numpy as np 

def function(x):

	r1 = x
	m9 = 1
	paths = []
	try:
		if x >= 0:
			x = x+3
			r1 = 5/r1
			paths.append(1)
		else:
			m9 = 6/m9
			paths.append(2)
		if x < 4:
			r1 = 5+9
			paths.append(3)
		else:
			m9 = x-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r1 = x**0.5
		return r1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))