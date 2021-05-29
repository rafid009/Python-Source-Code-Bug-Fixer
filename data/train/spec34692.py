import numpy as np 

def function(x):

	a9 = x
	e9 = 1
	paths = []
	try:
		if x < 2:
			e9 = 9-a9
			x = x*a9
			paths.append(1)
		else:
			a9 = 2-3
			x = x-x
			e9 = x+7
			paths.append(2)
		if a9 >= 3:
			x = 4/4
			x = x+e9
			a9 = 7*a9
			paths.append(3)
		else:
			a9 = a9+9
			paths.append(4)
		paths.append(5)
		assert a9 >= 0
		a9 = a9**0.5
		return a9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))