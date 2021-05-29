import numpy as np 

def function(x):

	n6 = x
	f3 = x
	paths = []
	try:
		if n6 >= 8:
			x = 0*4
			f3 = f3-f3
			paths.append(1)
		else:
			n6 = 3-f3
			f3 = 5*2
			paths.append(2)
		if f3 < 3:
			f3 = f3/7
			f3 = f3*3
			paths.append(3)
		else:
			f3 = 0-n6
			x = 1-x
			paths.append(4)
		paths.append(5)
		assert n6 >= 0
		n6 = n6**0.5
		return n6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))