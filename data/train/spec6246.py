import numpy as np 

def function(x):

	e4 = x
	j0 = x
	paths = []
	try:
		if j0 < 4:
			j0 = e4+j0
			x = 7/j0
			x = x-9
			paths.append(1)
		else:
			j0 = j0-5
			x = j0*3
			x = 0*x
			paths.append(2)
		if e4 < 3:
			x = 5*x
			paths.append(3)
		else:
			j0 = x-j0
			e4 = 3+j0
			x = x*2
			paths.append(4)
		paths.append(5)
		assert j0 >= 0
		j0 = j0**0.5
		return j0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))