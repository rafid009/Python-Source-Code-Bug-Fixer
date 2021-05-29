import numpy as np 

def function(x):

	j0 = 2
	n5 = x
	paths = []
	try:
		if n5 <= 1:
			x = 6+x
			x = x+6
			n5 = n5*9
			paths.append(1)
		else:
			j0 = 4/j0
			n5 = n5+8
			paths.append(2)
		if n5 < 9:
			x = 9*x
			n5 = 4/n5
			x = j0*4
			paths.append(3)
		else:
			j0 = j0-x
			paths.append(4)
		paths.append(5)
		assert j0 >= 0
		x = j0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))