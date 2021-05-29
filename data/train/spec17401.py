import numpy as np 

def function(x):

	a8 = 0
	l8 = x
	paths = []
	try:
		if l8 >= 6:
			a8 = a8/6
			paths.append(1)
		else:
			a8 = x*a8
			x = l8+x
			l8 = l8/7
			paths.append(2)
		if x > 4:
			x = a8-6
			l8 = 3+9
			paths.append(3)
		else:
			a8 = 8+8
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