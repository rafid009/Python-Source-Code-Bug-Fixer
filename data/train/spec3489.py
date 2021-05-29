import numpy as np 

def function(x):

	l2 = 4
	j9 = 2
	paths = []
	try:
		if x <= 9:
			l2 = l2-x
			paths.append(1)
		else:
			l2 = 6-6
			paths.append(2)
		if x >= 0:
			x = 9+x
			l2 = 9-9
			j9 = j9/4
			paths.append(3)
		else:
			j9 = 7-j9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j9 = x**0.5
		return j9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))