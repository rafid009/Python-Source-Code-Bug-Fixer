import numpy as np 

def function(x):

	v9 = x
	l6 = 3
	paths = []
	try:
		if l6 >= 0:
			l6 = l6-7
			x = 8-v9
			v9 = 8/v9
			paths.append(1)
		else:
			v9 = 8-v9
			l6 = l6+5
			paths.append(2)
		if v9 <= 1:
			v9 = 2-4
			paths.append(3)
		else:
			v9 = 0*2
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