import numpy as np 

def function(x):

	p3 = 4
	o4 = x
	x = 5
	paths = []
	try:
		if x > 0:
			x = x/o4
			o4 = o4/7
			paths.append(1)
		else:
			x = x*2
			x = x+o4
			p3 = 5*o4
			paths.append(2)
		if p3 <= 3:
			x = 2-2
			paths.append(3)
		else:
			o4 = p3/p3
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