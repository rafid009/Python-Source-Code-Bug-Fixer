import numpy as np 

def function(x):

	d0 = x
	p7 = x
	paths = []
	try:
		if p7 <= 6:
			x = d0/8
			d0 = 3/3
			paths.append(1)
		else:
			x = 6*0
			p7 = p7+3
			x = x-8
			paths.append(2)
		if x <= 0:
			x = d0+0
			paths.append(3)
		else:
			d0 = d0-d0
			x = 7-9
			p7 = p7/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p7 = x**0.5
		return p7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))