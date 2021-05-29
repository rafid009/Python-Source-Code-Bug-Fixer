import numpy as np 

def function(x):

	u7 = x
	a9 = 5
	paths = []
	try:
		if a9 >= 9:
			x = x/x
			u7 = 5/u7
			paths.append(1)
		else:
			u7 = a9/u7
			x = x+x
			paths.append(2)
		if a9 > 1:
			a9 = x-a9
			paths.append(3)
		else:
			x = x-3
			x = x+u7
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