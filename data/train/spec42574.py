import numpy as np 

def function(x):

	t6 = x
	x9 = x
	paths = []
	try:
		if t6 <= 1:
			x9 = x9+8
			x = x/x
			paths.append(1)
		else:
			x = 9*0
			x9 = x9-x
			paths.append(2)
		if t6 < 6:
			x = 9*x
			x9 = 5-x9
			x = x9*t6
			paths.append(3)
		else:
			x9 = x9/4
			x9 = t6-5
			x = x-x9
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		x9 = x9**0.5
		return x9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))