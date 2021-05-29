import numpy as np 

def function(x):

	x3 = 9
	x6 = x
	paths = []
	try:
		if x3 < 3:
			x6 = 9+x6
			x3 = x*x3
			paths.append(1)
		else:
			x = x*2
			x = x*5
			paths.append(2)
		if x6 >= 2:
			x = x+x6
			x = x6/2
			paths.append(3)
		else:
			x = 2-2
			x3 = x3/x6
			x6 = x3-8
			paths.append(4)
		paths.append(5)
		assert x3 >= 0
		x6 = x3**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))