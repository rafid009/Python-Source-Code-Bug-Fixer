import numpy as np 

def function(x):

	a7 = x
	j0 = 9
	paths = []
	try:
		if a7 > 4:
			j0 = x+x
			j0 = j0*a7
			paths.append(1)
		else:
			j0 = a7+j0
			a7 = j0-2
			a7 = 9+a7
			paths.append(2)
		if x > 3:
			x = 8+x
			paths.append(3)
		else:
			j0 = x+5
			j0 = 7/j0
			a7 = 2*4
			paths.append(4)
		paths.append(5)
		assert j0 >= 0
		a7 = j0**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))