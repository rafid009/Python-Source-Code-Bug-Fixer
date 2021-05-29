import numpy as np 

def function(x):

	d8 = x
	f7 = 0
	paths = []
	try:
		if d8 <= 8:
			d8 = d8+7
			paths.append(1)
		else:
			d8 = d8-2
			x = d8-9
			paths.append(2)
		if x < 8:
			d8 = d8/2
			paths.append(3)
		else:
			f7 = 4*6
			f7 = x-f7
			x = x/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f7 = x**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))