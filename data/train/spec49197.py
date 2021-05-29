import numpy as np 

def function(x):

	v1 = 5
	l7 = 0
	paths = []
	try:
		if v1 < 2:
			x = x+5
			paths.append(1)
		else:
			l7 = 5-v1
			l7 = l7*l7
			v1 = 0-v1
			paths.append(2)
		if v1 < 3:
			v1 = 1+v1
			x = v1/x
			v1 = l7-v1
			paths.append(3)
		else:
			l7 = l7+0
			x = x/7
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