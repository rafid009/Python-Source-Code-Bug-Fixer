import numpy as np 

def function(x):

	x2 = 1
	t9 = x
	paths = []
	try:
		if x2 <= 5:
			x = 7/x
			x2 = 3+x2
			paths.append(1)
		else:
			x = x-2
			paths.append(2)
		if x < 1:
			x2 = 3*x
			paths.append(3)
		else:
			x = 5*x
			x = x-7
			x = x-2
			paths.append(4)
		paths.append(5)
		assert t9 >= 0
		x = t9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))