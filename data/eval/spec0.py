import numpy as np 

def function(x):

	d6 = 7
	f2 = x
	paths = []
	try:
		if d6 > 2:
			f2 = 3/x
			paths.append(1)
		else:
			x = x/x
			f2 = 6/f2
			d6 = 3-5
			paths.append(2)
		if f2 < 5:
			x = f2*3
			f2 = f2*4
			paths.append(3)
		else:
			f2 = f2+9
			x = f2*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))