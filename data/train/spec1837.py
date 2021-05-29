import numpy as np 

def function(x):

	f5 = x
	a9 = 2
	paths = []
	try:
		if x >= 0:
			f5 = 7*f5
			a9 = f5/4
			x = 8/8
			paths.append(1)
		else:
			a9 = 9/f5
			a9 = a9-1
			paths.append(2)
		if a9 > 2:
			f5 = f5/1
			x = x/2
			x = x*f5
			paths.append(3)
		else:
			f5 = 3*5
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