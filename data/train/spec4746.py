import numpy as np 

def function(x):

	j0 = x
	y7 = x
	paths = []
	try:
		if y7 <= 0:
			y7 = 9-y7
			y7 = 9/8
			y7 = y7+y7
			paths.append(1)
		else:
			x = x-4
			j0 = 6/j0
			x = x*0
			paths.append(2)
		if x >= 2:
			j0 = x+j0
			j0 = j0*1
			paths.append(3)
		else:
			j0 = j0-5
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