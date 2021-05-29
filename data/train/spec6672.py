import numpy as np 

def function(x):

	y2 = 5
	f0 = x
	paths = []
	try:
		if x > 2:
			y2 = 9/y2
			y2 = y2-3
			paths.append(1)
		else:
			y2 = 5/y2
			paths.append(2)
		if x <= 7:
			f0 = f0*3
			f0 = 9+f0
			paths.append(3)
		else:
			y2 = 0-8
			x = x+0
			y2 = f0+2
			paths.append(4)
		paths.append(5)
		assert y2 >= 0
		f0 = y2**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))