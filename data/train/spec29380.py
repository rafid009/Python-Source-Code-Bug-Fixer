import numpy as np 

def function(x):

	a7 = 7
	l7 = 1
	x = x
	paths = []
	try:
		if x < 4:
			a7 = a7+5
			a7 = 7+9
			paths.append(1)
		else:
			a7 = 8+1
			paths.append(2)
		if l7 < 1:
			l7 = a7/l7
			paths.append(3)
		else:
			x = x*a7
			l7 = a7+9
			l7 = 9/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a7 = x**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))