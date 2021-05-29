import numpy as np 

def function(x):

	d2 = x
	f9 = x
	x = x
	paths = []
	try:
		if d2 <= 6:
			f9 = f9-4
			paths.append(1)
		else:
			f9 = 5/f9
			paths.append(2)
		if f9 >= 1:
			f9 = x*6
			paths.append(3)
		else:
			f9 = 1*7
			paths.append(4)
		paths.append(5)
		assert d2 >= 0
		x = d2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))