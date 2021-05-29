import numpy as np 

def function(x):

	d6 = 0
	o8 = 7
	paths = []
	try:
		if x >= 0:
			o8 = o8*x
			o8 = d6/x
			x = x/2
			paths.append(1)
		else:
			d6 = 4-8
			x = x+6
			x = 4*x
			paths.append(2)
		if o8 <= 2:
			d6 = d6+d6
			o8 = 0*8
			o8 = 3*o8
			paths.append(3)
		else:
			d6 = d6+3
			o8 = o8*6
			paths.append(4)
		paths.append(5)
		assert d6 >= 0
		x = d6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))