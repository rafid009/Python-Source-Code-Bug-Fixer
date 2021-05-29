import numpy as np 

def function(x):

	x6 = 0
	n7 = 3
	paths = []
	try:
		if n7 < 0:
			x6 = 1-x6
			x6 = x6+1
			paths.append(1)
		else:
			n7 = 2*7
			n7 = n7*x
			n7 = x6*x
			paths.append(2)
		if x6 >= 7:
			x6 = 9+1
			x6 = x6/2
			paths.append(3)
		else:
			x6 = x+x6
			n7 = n7-n7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))