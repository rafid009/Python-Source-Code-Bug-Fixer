import numpy as np 

def function(x):

	x8 = 6
	d8 = x
	paths = []
	try:
		if d8 > 7:
			x8 = 2+5
			x8 = x8*4
			paths.append(1)
		else:
			x = x-1
			x8 = x8-1
			paths.append(2)
		if d8 <= 9:
			d8 = 7*x
			x = 4/x
			paths.append(3)
		else:
			x8 = x8*9
			x = 3*2
			x = x/4
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