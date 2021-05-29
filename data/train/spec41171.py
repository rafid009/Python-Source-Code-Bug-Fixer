import numpy as np 

def function(x):

	f6 = x
	n6 = x
	paths = []
	try:
		if n6 > 8:
			f6 = f6-2
			f6 = 4+9
			paths.append(1)
		else:
			x = x+n6
			x = 8*x
			paths.append(2)
		if n6 > 0:
			f6 = 0-f6
			paths.append(3)
		else:
			f6 = 0/f6
			n6 = n6-x
			paths.append(4)
		paths.append(5)
		assert f6 >= 0
		n6 = f6**0.5
		return n6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))