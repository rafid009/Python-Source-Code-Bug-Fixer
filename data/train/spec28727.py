import numpy as np 

def function(x):

	j5 = x
	x0 = 1
	paths = []
	try:
		if x0 > 7:
			j5 = j5-9
			j5 = j5/5
			paths.append(1)
		else:
			j5 = 7+j5
			x0 = x0*7
			j5 = 8/5
			paths.append(2)
		if x <= 4:
			x0 = j5-6
			paths.append(3)
		else:
			x = 0*x
			paths.append(4)
		paths.append(5)
		assert x0 >= 0
		x0 = x0**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))