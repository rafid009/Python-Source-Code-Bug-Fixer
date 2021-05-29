import numpy as np 

def function(x):

	j0 = x
	e6 = 4
	paths = []
	try:
		if e6 >= 3:
			j0 = j0-0
			j0 = j0+8
			j0 = j0-j0
			paths.append(1)
		else:
			x = 7+4
			j0 = e6/e6
			x = 2+1
			paths.append(2)
		if j0 > 9:
			x = x-2
			paths.append(3)
		else:
			j0 = j0+x
			e6 = 6*e6
			paths.append(4)
		paths.append(5)
		assert j0 >= 0
		e6 = j0**0.5
		return e6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))