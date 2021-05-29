import numpy as np 

def function(x):

	a9 = x
	y5 = 3
	x = 5
	paths = []
	try:
		if x < 6:
			x = 4/6
			x = x/8
			x = 5/x
			paths.append(1)
		else:
			x = 2-6
			a9 = a9*y5
			x = 2-x
			paths.append(2)
		if y5 >= 1:
			y5 = 3+y5
			x = x*x
			paths.append(3)
		else:
			a9 = 8*x
			a9 = a9-7
			a9 = a9/9
			paths.append(4)
		paths.append(5)
		assert a9 >= 0
		x = a9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))