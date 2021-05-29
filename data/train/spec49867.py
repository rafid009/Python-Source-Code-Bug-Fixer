import numpy as np 

def function(x):

	a5 = x
	a2 = x
	x = 1
	paths = []
	try:
		if a2 >= 5:
			a5 = 4+2
			a5 = 5*a5
			paths.append(1)
		else:
			a2 = a2*9
			paths.append(2)
		if a5 >= 5:
			a2 = 8/a2
			a2 = a2*a2
			a2 = 9+5
			paths.append(3)
		else:
			x = 3*x
			a5 = a5/9
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		a5 = a5**0.5
		return a5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))