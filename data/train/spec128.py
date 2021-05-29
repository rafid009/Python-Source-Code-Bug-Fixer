import numpy as np 

def function(x):

	a4 = 0
	v6 = x
	paths = []
	try:
		if x > 8:
			a4 = 1/1
			v6 = 0/2
			a4 = 3+a4
			paths.append(1)
		else:
			a4 = a4*3
			v6 = 4/v6
			paths.append(2)
		if a4 > 4:
			a4 = a4*3
			v6 = v6/1
			a4 = a4+2
			paths.append(3)
		else:
			v6 = a4+a4
			v6 = 8*v6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v6 = x**0.5
		return v6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))