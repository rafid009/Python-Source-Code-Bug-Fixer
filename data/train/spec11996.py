import numpy as np 

def function(x):

	o0 = 9
	j0 = x
	paths = []
	try:
		if x >= 7:
			j0 = j0*2
			j0 = j0*3
			o0 = 9/o0
			paths.append(1)
		else:
			j0 = 1-x
			paths.append(2)
		if j0 >= 5:
			x = o0-9
			x = 9/6
			o0 = 1/j0
			paths.append(3)
		else:
			x = 8-j0
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