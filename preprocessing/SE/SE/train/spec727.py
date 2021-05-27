import numpy as np 

def function(x):

	f8 = x
	d2 = x
	x = 4
	paths = []
	try:
		if x <= 9:
			f8 = 3+d2
			paths.append(1)
		else:
			x = 6*x
			x = x/x
			paths.append(2)
		if f8 < 4:
			d2 = 8*d2
			d2 = x+2
			paths.append(3)
		else:
			f8 = f8/d2
			paths.append(4)
		paths.append(5)
		assert f8 >= 0
		x = f8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))