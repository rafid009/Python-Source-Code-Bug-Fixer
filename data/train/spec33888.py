import numpy as np 

def function(x):

	r8 = 2
	d6 = 2
	paths = []
	try:
		if d6 < 6:
			x = 0+x
			paths.append(1)
		else:
			r8 = x+0
			paths.append(2)
		if d6 <= 3:
			r8 = r8-5
			x = 2/x
			paths.append(3)
		else:
			r8 = r8+3
			d6 = 9+d6
			d6 = r8-4
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