import numpy as np 

def function(x):

	p2 = 6
	o7 = x
	paths = []
	try:
		if o7 > 3:
			o7 = o7*6
			x = 2-4
			paths.append(1)
		else:
			x = 6/x
			o7 = 2*p2
			o7 = 1/o7
			paths.append(2)
		if o7 < 8:
			x = x*6
			p2 = p2+p2
			x = x/7
			paths.append(3)
		else:
			p2 = p2/o7
			o7 = 4-o7
			x = x/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o7 = x**0.5
		return o7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))