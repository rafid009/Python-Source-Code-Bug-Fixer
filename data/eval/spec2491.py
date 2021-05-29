import numpy as np 

def function(x):

	d3 = x
	o2 = 2
	paths = []
	try:
		if x <= 5:
			o2 = 9/5
			o2 = 5*o2
			x = x+d3
			paths.append(1)
		else:
			x = x*5
			paths.append(2)
		if x < 1:
			o2 = o2/5
			d3 = 6+6
			d3 = x+d3
			paths.append(3)
		else:
			o2 = o2*2
			x = 0*o2
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