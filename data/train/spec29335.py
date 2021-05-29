import numpy as np 

def function(x):

	m0 = x
	r9 = x
	paths = []
	try:
		if r9 > 2:
			x = m0/7
			paths.append(1)
		else:
			r9 = 5*r9
			paths.append(2)
		if x > 1:
			r9 = x/r9
			paths.append(3)
		else:
			x = x/4
			paths.append(4)
		paths.append(5)
		assert r9 >= 0
		x = r9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))