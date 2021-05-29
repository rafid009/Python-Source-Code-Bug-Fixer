import numpy as np 

def function(x):

	d9 = x
	f9 = 6
	paths = []
	try:
		if d9 < 5:
			d9 = d9-x
			d9 = 5*d9
			paths.append(1)
		else:
			f9 = f9/8
			x = 5-x
			f9 = 0+9
			paths.append(2)
		if x >= 3:
			f9 = 5/3
			paths.append(3)
		else:
			d9 = d9+7
			f9 = x*4
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