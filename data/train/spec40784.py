import numpy as np 

def function(x):

	x6 = x
	n6 = 2
	paths = []
	try:
		if n6 <= 3:
			x = x*5
			x6 = x6-0
			paths.append(1)
		else:
			x6 = x6*2
			paths.append(2)
		if x < 0:
			n6 = n6+n6
			n6 = x*6
			x = 8/x6
			paths.append(3)
		else:
			n6 = n6*6
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