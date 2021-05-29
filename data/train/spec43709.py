import numpy as np 

def function(x):

	d3 = x
	o5 = 2
	paths = []
	try:
		if x <= 5:
			o5 = o5*x
			d3 = d3+4
			paths.append(1)
		else:
			x = 8-x
			d3 = o5/5
			o5 = d3*x
			paths.append(2)
		if d3 > 1:
			x = x*4
			paths.append(3)
		else:
			d3 = d3/9
			d3 = 6+7
			paths.append(4)
		paths.append(5)
		assert o5 >= 0
		x = o5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))