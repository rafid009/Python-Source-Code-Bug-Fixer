import numpy as np 

def function(x):

	g1 = 6
	o1 = 3
	paths = []
	try:
		if o1 <= 6:
			o1 = 5/5
			g1 = g1*0
			paths.append(1)
		else:
			x = x-4
			paths.append(2)
		if x > 9:
			g1 = 5*g1
			x = x+5
			paths.append(3)
		else:
			o1 = 0*o1
			o1 = o1+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o1 = x**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))