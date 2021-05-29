import numpy as np 

def function(x):

	a8 = 1
	a3 = x
	paths = []
	try:
		if a3 < 7:
			a8 = a8-x
			x = a3+4
			a8 = 4/a8
			paths.append(1)
		else:
			a8 = a8*a3
			a8 = 6*a8
			paths.append(2)
		if a3 <= 6:
			a3 = a3/4
			x = x*9
			x = 7+x
			paths.append(3)
		else:
			a3 = 3/a8
			a8 = 1-a8
			a3 = a3+5
			paths.append(4)
		paths.append(5)
		assert a3 >= 0
		a8 = a3**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))