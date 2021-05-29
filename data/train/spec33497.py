import numpy as np 

def function(x):

	a5 = x
	l3 = x
	paths = []
	try:
		if l3 <= 5:
			a5 = a5*4
			paths.append(1)
		else:
			a5 = 5/3
			a5 = 8-x
			paths.append(2)
		if l3 > 8:
			x = l3*4
			paths.append(3)
		else:
			a5 = x+8
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