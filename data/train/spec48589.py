import numpy as np 

def function(x):

	p5 = 1
	x1 = 2
	paths = []
	try:
		if x > 7:
			x1 = x1*1
			x1 = 7-x1
			paths.append(1)
		else:
			p5 = p5+7
			paths.append(2)
		if x1 >= 6:
			x1 = 0/4
			paths.append(3)
		else:
			x = 1-x
			x1 = 9/p5
			p5 = 9/p5
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