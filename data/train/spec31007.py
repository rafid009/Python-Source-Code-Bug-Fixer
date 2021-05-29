import numpy as np 

def function(x):

	a7 = 3
	p3 = x
	paths = []
	try:
		if x <= 6:
			p3 = a7-8
			x = x/4
			p3 = p3*9
			paths.append(1)
		else:
			a7 = x+p3
			paths.append(2)
		if x <= 8:
			p3 = 0/8
			a7 = a7/3
			paths.append(3)
		else:
			x = x*7
			a7 = 5/a7
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