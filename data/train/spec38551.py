import numpy as np 

def function(x):

	x2 = 5
	a9 = x
	paths = []
	try:
		if x2 >= 9:
			x = 3*1
			a9 = a9+a9
			paths.append(1)
		else:
			x2 = x2/x2
			x = x-0
			paths.append(2)
		if x < 3:
			x = 5-x
			paths.append(3)
		else:
			x = x*a9
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