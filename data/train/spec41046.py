import numpy as np 

def function(x):

	l3 = 5
	j9 = x
	paths = []
	try:
		if j9 <= 6:
			j9 = 0-l3
			paths.append(1)
		else:
			l3 = x/l3
			paths.append(2)
		if j9 <= 4:
			x = x/8
			j9 = l3-j9
			paths.append(3)
		else:
			l3 = 9*9
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