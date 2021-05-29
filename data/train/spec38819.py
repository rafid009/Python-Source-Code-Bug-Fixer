import numpy as np 

def function(x):

	i7 = x
	l8 = 2
	paths = []
	try:
		if l8 >= 3:
			i7 = 0/x
			l8 = l8*l8
			l8 = l8*x
			paths.append(1)
		else:
			x = x+i7
			paths.append(2)
		if x <= 1:
			l8 = i7+x
			x = i7/9
			paths.append(3)
		else:
			l8 = l8/x
			x = 8-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l8 = x**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))