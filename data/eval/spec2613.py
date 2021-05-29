import numpy as np 

def function(x):

	o9 = 1
	v6 = 2
	paths = []
	try:
		if o9 < 6:
			o9 = 1*4
			x = x*5
			paths.append(1)
		else:
			v6 = v6/v6
			o9 = x+x
			paths.append(2)
		if x < 6:
			x = 2-o9
			o9 = o9*o9
			v6 = x+o9
			paths.append(3)
		else:
			x = x/o9
			x = x/6
			o9 = o9+9
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