import numpy as np 

def function(x):

	d7 = 2
	o7 = x
	paths = []
	try:
		if x <= 8:
			x = d7*2
			d7 = 2/d7
			d7 = 7*9
			paths.append(1)
		else:
			x = x-1
			o7 = 3-o7
			paths.append(2)
		if d7 < 5:
			o7 = x/d7
			o7 = 6*o7
			paths.append(3)
		else:
			o7 = 0+o7
			paths.append(4)
		paths.append(5)
		assert o7 >= 0
		o7 = o7**0.5
		return o7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))