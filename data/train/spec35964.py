import numpy as np 

def function(x):

	p2 = x
	o4 = x
	paths = []
	try:
		if p2 >= 2:
			p2 = p2+0
			paths.append(1)
		else:
			x = 9+x
			paths.append(2)
		if o4 > 3:
			p2 = x-9
			x = 2*0
			o4 = o4-x
			paths.append(3)
		else:
			o4 = 1+x
			x = p2+x
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