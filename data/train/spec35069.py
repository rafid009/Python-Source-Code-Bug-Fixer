import numpy as np 

def function(x):

	d7 = x
	f0 = 2
	x = x
	paths = []
	try:
		if d7 >= 9:
			d7 = 6+f0
			d7 = d7*f0
			paths.append(1)
		else:
			d7 = 3-x
			x = x/d7
			paths.append(2)
		if d7 > 7:
			d7 = d7*x
			paths.append(3)
		else:
			f0 = f0-5
			x = 2/x
			paths.append(4)
		paths.append(5)
		assert f0 >= 0
		d7 = f0**0.5
		return d7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))