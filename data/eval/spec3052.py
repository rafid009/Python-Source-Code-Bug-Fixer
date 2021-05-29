import numpy as np 

def function(x):

	e3 = x
	l5 = 3
	paths = []
	try:
		if x >= 4:
			l5 = l5+l5
			x = x/9
			e3 = 5/8
			paths.append(1)
		else:
			l5 = e3/l5
			x = x+l5
			l5 = l5-6
			paths.append(2)
		if x >= 2:
			e3 = 8/7
			x = l5/e3
			x = x*7
			paths.append(3)
		else:
			x = x/e3
			e3 = 1/6
			l5 = l5-e3
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