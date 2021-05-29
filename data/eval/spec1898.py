import numpy as np 

def function(x):

	x6 = 9
	x2 = x
	paths = []
	try:
		if x6 < 0:
			x = x2/x
			paths.append(1)
		else:
			x2 = x6/x2
			x = x+2
			x = x2/8
			paths.append(2)
		if x2 > 5:
			x6 = 3-x2
			x2 = x6-x2
			x6 = x2+7
			paths.append(3)
		else:
			x6 = x*x6
			paths.append(4)
		paths.append(5)
		assert x6 >= 0
		x = x6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))