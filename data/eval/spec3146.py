import numpy as np 

def function(x):

	q4 = 4
	f0 = x
	paths = []
	try:
		if f0 < 9:
			f0 = 1/f0
			q4 = 4/q4
			x = 7-x
			paths.append(1)
		else:
			f0 = f0+5
			f0 = f0/7
			paths.append(2)
		if q4 > 0:
			q4 = q4/f0
			paths.append(3)
		else:
			f0 = 0/f0
			f0 = f0*f0
			paths.append(4)
		paths.append(5)
		assert q4 >= 0
		x = q4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))