import numpy as np 

def function(x):

	e5 = 7
	l8 = x
	paths = []
	try:
		if l8 >= 0:
			l8 = l8/e5
			e5 = l8/e5
			x = x-2
			paths.append(1)
		else:
			l8 = 6+l8
			e5 = l8+e5
			paths.append(2)
		if x <= 7:
			e5 = 5-x
			e5 = e5*2
			paths.append(3)
		else:
			x = 1*8
			paths.append(4)
		paths.append(5)
		assert l8 >= 0
		l8 = l8**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))