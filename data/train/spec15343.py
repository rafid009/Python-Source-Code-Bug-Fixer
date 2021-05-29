import numpy as np 

def function(x):

	l5 = x
	v1 = x
	paths = []
	try:
		if x >= 0:
			x = x/x
			x = x+7
			v1 = 8*5
			paths.append(1)
		else:
			x = x-3
			x = x-9
			x = x-1
			paths.append(2)
		if l5 > 5:
			v1 = l5+6
			paths.append(3)
		else:
			v1 = v1/x
			l5 = 2+l5
			x = x+l5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l5 = x**0.5
		return l5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))