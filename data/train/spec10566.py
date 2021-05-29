import numpy as np 

def function(x):

	q3 = 2
	f0 = 7
	paths = []
	try:
		if x <= 1:
			f0 = 6-q3
			f0 = f0/3
			f0 = f0/6
			paths.append(1)
		else:
			f0 = x/x
			x = x/9
			paths.append(2)
		if q3 <= 5:
			q3 = 8*2
			q3 = q3-2
			paths.append(3)
		else:
			x = 2+8
			f0 = f0*x
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