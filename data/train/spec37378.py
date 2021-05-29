import numpy as np 

def function(x):

	l8 = x
	a1 = 5
	paths = []
	try:
		if l8 >= 7:
			a1 = a1*6
			a1 = a1-5
			l8 = l8/a1
			paths.append(1)
		else:
			a1 = 3-l8
			x = x+5
			paths.append(2)
		if a1 < 7:
			a1 = 9*1
			paths.append(3)
		else:
			a1 = a1/9
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