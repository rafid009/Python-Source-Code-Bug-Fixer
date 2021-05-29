import numpy as np 

def function(x):

	f2 = 6
	u2 = 7
	paths = []
	try:
		if x < 3:
			u2 = x-4
			f2 = 2-4
			u2 = 7+x
			paths.append(1)
		else:
			f2 = 1+f2
			u2 = u2/u2
			u2 = 3*u2
			paths.append(2)
		if u2 > 0:
			u2 = 1*x
			paths.append(3)
		else:
			u2 = u2*x
			paths.append(4)
		paths.append(5)
		assert u2 >= 0
		x = u2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))