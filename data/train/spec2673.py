import numpy as np 

def function(x):

	n7 = x
	x9 = x
	x = 0
	paths = []
	try:
		if x9 <= 8:
			x9 = x9/7
			x9 = 6+x9
			x = x/8
			paths.append(1)
		else:
			x = x-8
			paths.append(2)
		if n7 < 8:
			x9 = 9+x9
			x9 = x9+0
			paths.append(3)
		else:
			n7 = n7/n7
			paths.append(4)
		paths.append(5)
		assert n7 >= 0
		x = n7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))