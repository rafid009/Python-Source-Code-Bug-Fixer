import numpy as np 

def function(x):

	a6 = 4
	p2 = 2
	paths = []
	try:
		if a6 <= 2:
			x = x-9
			paths.append(1)
		else:
			x = x*2
			a6 = 3/8
			paths.append(2)
		if a6 > 4:
			p2 = p2/7
			x = x/4
			paths.append(3)
		else:
			x = x/a6
			p2 = 6+p2
			a6 = 6*a6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a6 = x**0.5
		return a6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))