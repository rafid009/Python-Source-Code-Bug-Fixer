import numpy as np 

def function(x):

	p0 = 5
	o4 = 7
	x = x
	paths = []
	try:
		if x < 5:
			p0 = p0/p0
			paths.append(1)
		else:
			x = 4+0
			paths.append(2)
		if o4 >= 1:
			x = x*9
			p0 = x*p0
			paths.append(3)
		else:
			p0 = p0+5
			p0 = p0/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o4 = x**0.5
		return o4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))