import numpy as np 

def function(x):

	y8 = x
	j5 = 8
	paths = []
	try:
		if x > 1:
			y8 = x*9
			j5 = j5/7
			x = 8-x
			paths.append(1)
		else:
			y8 = 2*4
			j5 = 9+y8
			x = y8/5
			paths.append(2)
		if x <= 6:
			j5 = x/j5
			paths.append(3)
		else:
			j5 = x*j5
			j5 = x*y8
			x = 5+x
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