import numpy as np 

def function(x):

	f6 = x
	n9 = x
	paths = []
	try:
		if x >= 9:
			f6 = f6/3
			n9 = 0+1
			paths.append(1)
		else:
			n9 = n9-x
			f6 = f6+f6
			paths.append(2)
		if n9 >= 4:
			n9 = 0+n9
			paths.append(3)
		else:
			x = x-3
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