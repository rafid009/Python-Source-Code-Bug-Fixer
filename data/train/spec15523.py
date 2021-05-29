import numpy as np 

def function(x):

	v1 = x
	a3 = 3
	paths = []
	try:
		if v1 > 7:
			v1 = 2*v1
			paths.append(1)
		else:
			a3 = a3-5
			v1 = 7/v1
			v1 = v1-a3
			paths.append(2)
		if a3 >= 8:
			x = x*3
			x = x*5
			paths.append(3)
		else:
			v1 = x-0
			x = 1/x
			paths.append(4)
		paths.append(5)
		assert a3 >= 0
		a3 = a3**0.5
		return a3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))