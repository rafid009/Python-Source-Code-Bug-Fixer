import numpy as np 

def function(x):

	a6 = 9
	p3 = x
	paths = []
	try:
		if x <= 9:
			a6 = a6/7
			p3 = 2-p3
			paths.append(1)
		else:
			p3 = p3-3
			a6 = x+a6
			a6 = a6*4
			paths.append(2)
		if a6 > 1:
			a6 = 1+a6
			x = 6/p3
			paths.append(3)
		else:
			x = x/8
			p3 = 3-4
			paths.append(4)
		paths.append(5)
		assert p3 >= 0
		x = p3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))