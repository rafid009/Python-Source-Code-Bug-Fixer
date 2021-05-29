import numpy as np 

def function(x):

	x4 = x
	p3 = 2
	paths = []
	try:
		if x4 >= 0:
			x = x-2
			p3 = 9/p3
			paths.append(1)
		else:
			x4 = 9*x4
			x4 = x4/2
			paths.append(2)
		if p3 > 9:
			x4 = x4*4
			x = x4-8
			paths.append(3)
		else:
			p3 = p3-6
			x = x+x
			p3 = p3-8
			paths.append(4)
		paths.append(5)
		assert p3 >= 0
		x4 = p3**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))