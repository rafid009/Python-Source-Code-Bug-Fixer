import numpy as np 

def function(x):

	a3 = x
	j5 = x
	paths = []
	try:
		if x > 2:
			x = 1+j5
			a3 = x+j5
			x = 9+x
			paths.append(1)
		else:
			x = a3-a3
			a3 = 1+a3
			paths.append(2)
		if a3 > 1:
			a3 = 8-x
			x = a3+x
			paths.append(3)
		else:
			a3 = a3/7
			paths.append(4)
		paths.append(5)
		assert a3 >= 0
		x = a3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))