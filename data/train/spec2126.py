import numpy as np 

def function(x):

	v3 = 2
	p6 = 4
	paths = []
	try:
		if x <= 3:
			v3 = 4-2
			v3 = v3-v3
			v3 = x+v3
			paths.append(1)
		else:
			p6 = 0+6
			paths.append(2)
		if p6 >= 1:
			x = x-6
			paths.append(3)
		else:
			p6 = p6*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p6 = x**0.5
		return p6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))