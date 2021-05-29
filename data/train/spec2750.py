import numpy as np 

def function(x):

	f2 = x
	k2 = 8
	paths = []
	try:
		if f2 >= 5:
			x = x/9
			x = 8/x
			paths.append(1)
		else:
			f2 = f2/8
			f2 = 4*f2
			f2 = k2/f2
			paths.append(2)
		if x <= 1:
			k2 = k2*5
			paths.append(3)
		else:
			f2 = f2-0
			k2 = x/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k2 = x**0.5
		return k2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))