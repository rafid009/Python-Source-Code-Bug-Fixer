import numpy as np 

def function(x):

	x0 = x
	j5 = 5
	paths = []
	try:
		if x <= 9:
			x0 = x0+x0
			x0 = 3-x0
			j5 = 6+j5
			paths.append(1)
		else:
			j5 = j5-7
			paths.append(2)
		if x0 >= 1:
			x0 = x0/9
			j5 = 7+j5
			j5 = j5/1
			paths.append(3)
		else:
			x0 = j5+2
			x = 8-8
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