import numpy as np 

def function(x):

	f8 = x
	d1 = 7
	paths = []
	try:
		if f8 >= 1:
			f8 = d1/f8
			d1 = 1-5
			paths.append(1)
		else:
			f8 = f8-7
			d1 = f8+x
			d1 = 6*d1
			paths.append(2)
		if d1 < 8:
			f8 = f8/x
			paths.append(3)
		else:
			f8 = 2*d1
			paths.append(4)
		paths.append(5)
		assert f8 >= 0
		d1 = f8**0.5
		return d1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))