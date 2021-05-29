import numpy as np 

def function(x):

	p5 = x
	a1 = 5
	paths = []
	try:
		if p5 > 2:
			a1 = p5*2
			a1 = 7/3
			paths.append(1)
		else:
			a1 = a1-2
			paths.append(2)
		if p5 > 2:
			a1 = 1*x
			x = 8*x
			p5 = 9+p5
			paths.append(3)
		else:
			a1 = a1/x
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