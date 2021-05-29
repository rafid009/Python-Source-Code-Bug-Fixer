import numpy as np 

def function(x):

	x5 = x
	paths = []
	try:
		if x5 < 4:
			x5 = x5*x5
			x = x5+9
			paths.append(1)
		else:
			x = 9+x5
			paths.append(2)
		if x > 0:
			x5 = x5-x
			paths.append(3)
		else:
			x = 6*0
			x5 = 4-x5
			x = 9*x
			paths.append(4)
		paths.append(5)
		assert x5 >= 0
		x5 = x5**0.5
		return x5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))