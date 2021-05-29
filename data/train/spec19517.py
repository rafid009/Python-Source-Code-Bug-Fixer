import numpy as np 

def function(x):

	f7 = 5
	j0 = 7
	paths = []
	try:
		if j0 <= 3:
			x = 7+x
			f7 = 8/6
			paths.append(1)
		else:
			f7 = 2-f7
			x = x-5
			x = 5-x
			paths.append(2)
		if f7 < 1:
			x = x-j0
			paths.append(3)
		else:
			x = 3*x
			f7 = f7-7
			j0 = 0/j0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j0 = x**0.5
		return j0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))