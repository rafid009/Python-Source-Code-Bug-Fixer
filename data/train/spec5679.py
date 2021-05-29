import numpy as np 

def function(x):

	y5 = 2
	p3 = 5
	paths = []
	try:
		if p3 >= 2:
			p3 = 9-8
			p3 = p3*3
			p3 = p3+p3
			paths.append(1)
		else:
			x = p3-x
			x = x/y5
			p3 = 9/6
			paths.append(2)
		if p3 >= 5:
			x = x+0
			paths.append(3)
		else:
			y5 = y5/p3
			y5 = y5*p3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p3 = x**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))