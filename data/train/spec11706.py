import numpy as np 

def function(x):

	d1 = x
	f9 = x
	paths = []
	try:
		if d1 <= 9:
			d1 = 2+d1
			paths.append(1)
		else:
			x = x*6
			f9 = f9+4
			paths.append(2)
		if d1 >= 3:
			x = x+1
			paths.append(3)
		else:
			f9 = f9-8
			d1 = 9*f9
			f9 = 8-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f9 = x**0.5
		return f9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))