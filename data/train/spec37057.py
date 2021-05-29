import numpy as np 

def function(x):

	p3 = 8
	d2 = 9
	paths = []
	try:
		if x >= 2:
			d2 = d2*0
			x = x+9
			paths.append(1)
		else:
			d2 = 9-1
			paths.append(2)
		if p3 > 9:
			p3 = 5*p3
			paths.append(3)
		else:
			x = x-2
			p3 = 6*0
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