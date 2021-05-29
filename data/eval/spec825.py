import numpy as np 

def function(x):

	x5 = x
	n9 = 6
	paths = []
	try:
		if x < 5:
			x = 9/x5
			x = x5+n9
			n9 = 8*n9
			paths.append(1)
		else:
			x = x*5
			x = x-6
			x = 6/5
			paths.append(2)
		if x < 3:
			n9 = 8+n9
			x = 3+x
			paths.append(3)
		else:
			x = x/5
			x = x5-7
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