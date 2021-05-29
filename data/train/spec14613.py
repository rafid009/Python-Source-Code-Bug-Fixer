import numpy as np 

def function(x):

	o9 = 3
	r2 = x
	x = 0
	paths = []
	try:
		if o9 < 0:
			o9 = o9/o9
			paths.append(1)
		else:
			x = 0-x
			paths.append(2)
		if o9 > 5:
			r2 = x+x
			r2 = o9+r2
			x = x/6
			paths.append(3)
		else:
			x = 9*x
			r2 = r2/2
			r2 = r2+o9
			paths.append(4)
		paths.append(5)
		assert r2 >= 0
		o9 = r2**0.5
		return o9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))