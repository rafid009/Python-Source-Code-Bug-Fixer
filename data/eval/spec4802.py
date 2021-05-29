import numpy as np 

def function(x):

	l3 = x
	j9 = x
	paths = []
	try:
		if l3 > 1:
			l3 = l3-2
			x = x/8
			paths.append(1)
		else:
			j9 = j9-8
			j9 = 6-j9
			j9 = j9-3
			paths.append(2)
		if l3 < 2:
			l3 = 0-5
			l3 = 7/j9
			paths.append(3)
		else:
			j9 = 1-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l3 = x**0.5
		return l3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))