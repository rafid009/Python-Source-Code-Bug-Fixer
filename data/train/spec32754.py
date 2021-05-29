import numpy as np 

def function(x):

	n6 = x
	f7 = 6
	paths = []
	try:
		if f7 > 3:
			f7 = f7/n6
			x = x+3
			x = 4+n6
			paths.append(1)
		else:
			x = 9*x
			paths.append(2)
		if x <= 0:
			f7 = n6*f7
			n6 = n6+n6
			f7 = f7/5
			paths.append(3)
		else:
			f7 = x*f7
			paths.append(4)
		paths.append(5)
		assert f7 >= 0
		x = f7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))