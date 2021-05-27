import numpy as np 

def function(x):

	o7 = x
	d9 = x
	paths = []
	try:
		if x <= 8:
			x = 2/x
			d9 = o7*1
			x = x/9
			paths.append(1)
		else:
			d9 = d9*x
			o7 = o7-o7
			paths.append(2)
		if o7 >= 8:
			x = 0*x
			paths.append(3)
		else:
			x = 0+x
			paths.append(4)
		paths.append(5)
		assert d9 >= 0
		o7 = d9**0.5
		return o7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))