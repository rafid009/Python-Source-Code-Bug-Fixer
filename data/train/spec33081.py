import numpy as np 

def function(x):

	a3 = x
	l7 = x
	paths = []
	try:
		if l7 >= 8:
			x = x-x
			a3 = 7/a3
			a3 = a3*8
			paths.append(1)
		else:
			l7 = l7+1
			paths.append(2)
		if l7 <= 0:
			l7 = 0/2
			x = l7/8
			x = x-x
			paths.append(3)
		else:
			x = x/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a3 = x**0.5
		return a3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))