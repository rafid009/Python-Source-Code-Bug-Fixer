import numpy as np 

def function(x):

	f1 = x
	u2 = 3
	paths = []
	try:
		if f1 < 1:
			f1 = f1+4
			paths.append(1)
		else:
			u2 = u2/u2
			paths.append(2)
		if x < 0:
			u2 = u2*4
			paths.append(3)
		else:
			f1 = 5/f1
			u2 = 1-x
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