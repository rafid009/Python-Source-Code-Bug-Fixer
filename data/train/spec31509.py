import numpy as np 

def function(x):

	x1 = x
	a7 = x
	paths = []
	try:
		if x > 4:
			x = x/9
			a7 = a7*a7
			x = 8+x
			paths.append(1)
		else:
			x = x*7
			paths.append(2)
		if x > 1:
			a7 = 4*a7
			x = x/5
			x = 7+x
			paths.append(3)
		else:
			x1 = x1*x1
			x = x-5
			x1 = 8-x1
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		x = a7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))