import numpy as np 

def function(x):

	d2 = x
	j5 = x
	paths = []
	try:
		if j5 > 2:
			j5 = 9+j5
			x = x-j5
			paths.append(1)
		else:
			j5 = j5+8
			paths.append(2)
		if d2 >= 7:
			x = x*9
			x = x-x
			paths.append(3)
		else:
			d2 = 9-j5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j5 = x**0.5
		return j5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))