import numpy as np 

def function(x):

	p3 = 5
	a7 = x
	paths = []
	try:
		if p3 < 0:
			x = x+8
			paths.append(1)
		else:
			a7 = a7*1
			paths.append(2)
		if x <= 1:
			p3 = 5-p3
			paths.append(3)
		else:
			p3 = 6+p3
			p3 = 4*7
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