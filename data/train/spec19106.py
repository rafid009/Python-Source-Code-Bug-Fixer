import numpy as np 

def function(x):

	j7 = x
	r2 = 7
	paths = []
	try:
		if r2 >= 8:
			j7 = x-r2
			j7 = 8/j7
			paths.append(1)
		else:
			j7 = j7-2
			j7 = j7+6
			r2 = j7-9
			paths.append(2)
		if r2 >= 2:
			j7 = j7+r2
			j7 = j7/r2
			paths.append(3)
		else:
			x = 0/x
			r2 = r2/9
			paths.append(4)
		paths.append(5)
		assert r2 >= 0
		r2 = r2**0.5
		return r2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))