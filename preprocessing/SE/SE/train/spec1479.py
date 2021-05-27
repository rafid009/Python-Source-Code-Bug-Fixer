import numpy as np 

def function(x):

	e3 = x
	n5 = x
	paths = []
	try:
		if e3 > 4:
			x = x-5
			paths.append(1)
		else:
			e3 = e3/7
			x = 9+x
			paths.append(2)
		if e3 >= 2:
			n5 = e3*n5
			n5 = 1-n5
			paths.append(3)
		else:
			n5 = 1+n5
			x = x-e3
			e3 = e3+e3
			paths.append(4)
		paths.append(5)
		assert e3 >= 0
		x = e3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))