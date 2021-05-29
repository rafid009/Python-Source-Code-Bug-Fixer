import numpy as np 

def function(x):

	l9 = 6
	i9 = x
	paths = []
	try:
		if l9 >= 9:
			x = x/6
			paths.append(1)
		else:
			i9 = x+i9
			x = 3*x
			x = 4/x
			paths.append(2)
		if i9 < 0:
			x = i9/2
			l9 = l9-7
			paths.append(3)
		else:
			i9 = 0+5
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