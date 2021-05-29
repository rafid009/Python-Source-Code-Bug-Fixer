import numpy as np 

def function(x):

	f4 = x
	d8 = 9
	paths = []
	try:
		if f4 <= 5:
			d8 = d8-3
			f4 = f4*4
			paths.append(1)
		else:
			d8 = 7+5
			f4 = 1+f4
			x = x/d8
			paths.append(2)
		if f4 <= 5:
			d8 = 5+5
			d8 = d8/f4
			paths.append(3)
		else:
			f4 = d8/f4
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		d8 = f4**0.5
		return d8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))