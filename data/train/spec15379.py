import numpy as np 

def function(x):

	o0 = 6
	d1 = x
	paths = []
	try:
		if x > 5:
			o0 = o0+d1
			d1 = d1-3
			x = x*4
			paths.append(1)
		else:
			x = x*2
			d1 = d1-7
			d1 = 6+d1
			paths.append(2)
		if x < 5:
			x = 2/x
			paths.append(3)
		else:
			o0 = 7+3
			x = 1*1
			d1 = d1-9
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