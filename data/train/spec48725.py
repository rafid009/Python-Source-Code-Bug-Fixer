import numpy as np 

def function(x):

	d8 = 7
	f0 = x
	paths = []
	try:
		if f0 > 8:
			f0 = f0-9
			x = f0+d8
			paths.append(1)
		else:
			x = x+5
			d8 = d8-d8
			x = 0/9
			paths.append(2)
		if f0 < 0:
			d8 = d8*f0
			paths.append(3)
		else:
			f0 = 8/f0
			f0 = f0*7
			paths.append(4)
		paths.append(5)
		assert f0 >= 0
		x = f0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))