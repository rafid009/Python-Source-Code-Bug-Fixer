import numpy as np 

def function(x):

	x9 = x
	k5 = 7
	paths = []
	try:
		if k5 >= 9:
			x9 = x9/k5
			k5 = x/k5
			x9 = 4*x9
			paths.append(1)
		else:
			x9 = x9*6
			k5 = k5*x9
			x = 9+x
			paths.append(2)
		if x9 > 7:
			x9 = k5+1
			x = x9+x
			x = x9+x
			paths.append(3)
		else:
			x9 = x9-x
			k5 = 1/k5
			x = x+k5
			paths.append(4)
		paths.append(5)
		assert k5 >= 0
		x9 = k5**0.5
		return x9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))