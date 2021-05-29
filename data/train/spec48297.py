import numpy as np 

def function(x):

	y2 = x
	f9 = x
	paths = []
	try:
		if x > 1:
			f9 = 6-0
			f9 = 4*f9
			paths.append(1)
		else:
			x = 0*y2
			y2 = y2-2
			paths.append(2)
		if x > 3:
			y2 = y2+y2
			f9 = f9*y2
			paths.append(3)
		else:
			y2 = 3+y2
			y2 = y2-5
			x = x*f9
			paths.append(4)
		paths.append(5)
		assert y2 >= 0
		f9 = y2**0.5
		return f9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))