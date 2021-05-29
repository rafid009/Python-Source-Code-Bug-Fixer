import numpy as np 

def function(x):

	d9 = 7
	o7 = x
	paths = []
	try:
		if o7 < 1:
			o7 = o7-2
			x = 5/x
			x = x*x
			paths.append(1)
		else:
			d9 = 1-d9
			paths.append(2)
		if x >= 4:
			d9 = 3/x
			x = 1*o7
			d9 = d9*1
			paths.append(3)
		else:
			x = x+x
			d9 = 2-d9
			paths.append(4)
		paths.append(5)
		assert o7 >= 0
		x = o7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))