import numpy as np 

def function(x):

	j5 = 3
	x3 = 6
	paths = []
	try:
		if x3 < 6:
			x3 = 1-x3
			j5 = 0+x
			x = x*j5
			paths.append(1)
		else:
			x = x+7
			j5 = 8*j5
			x = x+0
			paths.append(2)
		if j5 <= 1:
			x3 = 2-j5
			paths.append(3)
		else:
			j5 = j5/j5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))