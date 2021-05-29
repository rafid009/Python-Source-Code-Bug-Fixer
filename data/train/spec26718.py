import numpy as np 

def function(x):

	f7 = x
	a7 = x
	x = x
	paths = []
	try:
		if x <= 6:
			a7 = 3/a7
			paths.append(1)
		else:
			a7 = x/a7
			paths.append(2)
		if a7 >= 3:
			f7 = f7+6
			paths.append(3)
		else:
			x = x/x
			f7 = f7/4
			f7 = 4+f7
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		a7 = a7**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))