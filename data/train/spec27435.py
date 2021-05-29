import numpy as np 

def function(x):

	d8 = x
	f4 = 9
	paths = []
	try:
		if d8 >= 4:
			d8 = 5/5
			f4 = f4/x
			x = x*x
			paths.append(1)
		else:
			f4 = 3*f4
			paths.append(2)
		if x <= 3:
			f4 = 6-2
			f4 = f4+f4
			x = 0+x
			paths.append(3)
		else:
			d8 = d8-f4
			x = 2-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d8 = x**0.5
		return d8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))