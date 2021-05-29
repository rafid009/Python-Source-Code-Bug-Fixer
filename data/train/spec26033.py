import numpy as np 

def function(x):

	o0 = x
	d5 = 3
	paths = []
	try:
		if x <= 6:
			x = x*9
			paths.append(1)
		else:
			x = x+2
			o0 = o0*x
			paths.append(2)
		if x <= 2:
			o0 = x+2
			x = 4-5
			paths.append(3)
		else:
			d5 = x*0
			o0 = 8*o0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d5 = x**0.5
		return d5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))