import numpy as np 

def function(x):

	l8 = x
	j6 = x
	paths = []
	try:
		if j6 > 5:
			x = x*6
			x = 9-x
			x = x-l8
			paths.append(1)
		else:
			x = 2*x
			x = l8/x
			x = x-2
			paths.append(2)
		if l8 <= 3:
			j6 = l8-j6
			paths.append(3)
		else:
			x = x/7
			x = l8+7
			j6 = 5-4
			paths.append(4)
		paths.append(5)
		assert l8 >= 0
		x = l8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))