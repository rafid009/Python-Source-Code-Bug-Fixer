import numpy as np 

def function(x):

	p8 = x
	a7 = x
	paths = []
	try:
		if p8 > 7:
			a7 = 3/a7
			a7 = a7*a7
			paths.append(1)
		else:
			p8 = x*p8
			paths.append(2)
		if x > 1:
			x = a7+x
			p8 = p8*7
			paths.append(3)
		else:
			a7 = 1+a7
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