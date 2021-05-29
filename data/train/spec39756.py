import numpy as np 

def function(x):

	x7 = 2
	a6 = x
	paths = []
	try:
		if a6 >= 9:
			a6 = a6+0
			x = a6/x
			paths.append(1)
		else:
			x7 = x7+9
			paths.append(2)
		if a6 > 3:
			x = x+6
			paths.append(3)
		else:
			x7 = x7*0
			x7 = a6+6
			paths.append(4)
		paths.append(5)
		assert x7 >= 0
		a6 = x7**0.5
		return a6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))