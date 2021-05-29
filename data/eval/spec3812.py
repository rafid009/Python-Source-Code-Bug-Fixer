import numpy as np 

def function(x):

	d2 = 9
	f4 = x
	paths = []
	try:
		if d2 > 2:
			d2 = 0*9
			paths.append(1)
		else:
			d2 = x+f4
			paths.append(2)
		if f4 < 2:
			f4 = f4+f4
			paths.append(3)
		else:
			d2 = d2+d2
			x = x-2
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		d2 = f4**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))