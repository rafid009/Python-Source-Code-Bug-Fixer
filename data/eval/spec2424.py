import numpy as np 

def function(x):

	j9 = 8
	r2 = 4
	paths = []
	try:
		if r2 <= 1:
			x = x-2
			paths.append(1)
		else:
			r2 = r2*x
			r2 = r2-4
			j9 = 7/3
			paths.append(2)
		if r2 <= 6:
			j9 = j9-j9
			j9 = j9-r2
			r2 = r2/2
			paths.append(3)
		else:
			j9 = 0-j9
			x = x-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j9 = x**0.5
		return j9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))