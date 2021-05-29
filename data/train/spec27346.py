import numpy as np 

def function(x):

	p5 = x
	x0 = 2
	paths = []
	try:
		if x <= 0:
			x0 = x0-0
			paths.append(1)
		else:
			x0 = 4/x0
			x = x*2
			paths.append(2)
		if p5 < 3:
			p5 = 8/p5
			x0 = x+x0
			paths.append(3)
		else:
			x0 = 7/x0
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