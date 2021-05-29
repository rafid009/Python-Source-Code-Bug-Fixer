import numpy as np 

def function(x):

	f5 = x
	a7 = 6
	x = 4
	paths = []
	try:
		if x <= 5:
			f5 = 7*f5
			x = 1*7
			paths.append(1)
		else:
			a7 = a7/a7
			a7 = 8/a7
			f5 = a7-3
			paths.append(2)
		if x <= 4:
			x = x+f5
			x = x-9
			paths.append(3)
		else:
			a7 = 7+x
			a7 = a7*f5
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