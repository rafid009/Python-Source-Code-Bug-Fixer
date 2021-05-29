import numpy as np 

def function(x):

	j5 = x
	i4 = x
	paths = []
	try:
		if x > 9:
			j5 = x/i4
			x = 3*j5
			j5 = j5/9
			paths.append(1)
		else:
			x = 9/2
			j5 = 7/j5
			paths.append(2)
		if x >= 3:
			j5 = 9*4
			j5 = 1+4
			paths.append(3)
		else:
			x = i4-i4
			x = 8-x
			i4 = j5-i4
			paths.append(4)
		paths.append(5)
		assert i4 >= 0
		x = i4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))