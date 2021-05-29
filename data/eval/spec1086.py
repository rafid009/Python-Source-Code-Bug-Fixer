import numpy as np 

def function(x):

	k5 = x
	e5 = 7
	paths = []
	try:
		if x <= 6:
			e5 = 9+e5
			k5 = 6+k5
			x = x-k5
			paths.append(1)
		else:
			e5 = e5*5
			e5 = 7+e5
			paths.append(2)
		if k5 >= 7:
			e5 = x+1
			e5 = 2*e5
			paths.append(3)
		else:
			e5 = 5+k5
			paths.append(4)
		paths.append(5)
		assert e5 >= 0
		x = e5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))