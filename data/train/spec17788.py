import numpy as np 

def function(x):

	v7 = x
	a3 = 2
	paths = []
	try:
		if a3 > 2:
			v7 = v7+v7
			x = v7/4
			x = 6*x
			paths.append(1)
		else:
			x = x/5
			paths.append(2)
		if x >= 7:
			a3 = x/a3
			x = 9/x
			a3 = 0-a3
			paths.append(3)
		else:
			x = 1*x
			v7 = 0+v7
			paths.append(4)
		paths.append(5)
		assert v7 >= 0
		a3 = v7**0.5
		return a3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))