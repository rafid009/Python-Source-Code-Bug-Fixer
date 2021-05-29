import numpy as np 

def function(x):

	j0 = x
	a7 = 3
	paths = []
	try:
		if j0 > 9:
			x = x/9
			j0 = j0*3
			j0 = a7/j0
			paths.append(1)
		else:
			a7 = j0/a7
			j0 = j0+a7
			x = 8*x
			paths.append(2)
		if x <= 8:
			a7 = x*6
			x = 8+a7
			paths.append(3)
		else:
			j0 = j0/j0
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