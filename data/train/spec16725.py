import numpy as np 

def function(x):

	l5 = x
	i6 = 2
	paths = []
	try:
		if i6 > 2:
			x = 9*x
			l5 = x*l5
			paths.append(1)
		else:
			i6 = 9-i6
			l5 = l5/4
			x = x*6
			paths.append(2)
		if i6 < 9:
			i6 = 4*5
			paths.append(3)
		else:
			x = x/i6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i6 = x**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))