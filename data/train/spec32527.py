import numpy as np 

def function(x):

	d7 = x
	f0 = x
	x = 6
	paths = []
	try:
		if f0 > 1:
			x = d7*3
			paths.append(1)
		else:
			d7 = f0*7
			d7 = 7/d7
			d7 = d7/9
			paths.append(2)
		if f0 < 8:
			x = x/1
			x = 4-f0
			x = 8*x
			paths.append(3)
		else:
			x = x-7
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