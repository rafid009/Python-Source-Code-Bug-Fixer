import numpy as np 

def function(x):

	a3 = 9
	l9 = x
	paths = []
	try:
		if a3 <= 4:
			x = 7+a3
			l9 = 9+x
			a3 = 3-a3
			paths.append(1)
		else:
			l9 = l9-1
			paths.append(2)
		if l9 <= 5:
			a3 = x-x
			paths.append(3)
		else:
			x = l9-x
			l9 = 4+l9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l9 = x**0.5
		return l9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))