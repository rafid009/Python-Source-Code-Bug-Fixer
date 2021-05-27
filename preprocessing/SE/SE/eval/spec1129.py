import numpy as np 

def function(x):

	v5 = 7
	l6 = x
	x = x
	paths = []
	try:
		if l6 > 3:
			l6 = 1/l6
			paths.append(1)
		else:
			v5 = 5+v5
			paths.append(2)
		if l6 > 5:
			x = x*4
			paths.append(3)
		else:
			l6 = l6-8
			l6 = l6-8
			x = x+0
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