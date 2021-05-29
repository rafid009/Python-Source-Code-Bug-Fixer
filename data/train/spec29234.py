import numpy as np 

def function(x):

	a2 = x
	j0 = 8
	paths = []
	try:
		if x < 4:
			a2 = 0*8
			paths.append(1)
		else:
			j0 = x-j0
			x = x+j0
			a2 = 0-a2
			paths.append(2)
		if a2 >= 1:
			j0 = j0-7
			a2 = 7/6
			j0 = j0/1
			paths.append(3)
		else:
			x = x+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a2 = x**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))