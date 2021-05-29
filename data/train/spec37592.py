import numpy as np 

def function(x):

	f0 = x
	u2 = x
	x = x
	paths = []
	try:
		if f0 < 6:
			u2 = 0/u2
			u2 = 1+u2
			x = x*6
			paths.append(1)
		else:
			f0 = f0-0
			paths.append(2)
		if u2 <= 7:
			u2 = u2+6
			u2 = u2+1
			paths.append(3)
		else:
			u2 = u2*f0
			u2 = u2-1
			f0 = f0/1
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