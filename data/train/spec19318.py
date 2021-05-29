import numpy as np 

def function(x):

	f3 = 3
	z1 = 9
	paths = []
	try:
		if z1 > 0:
			f3 = z1-8
			paths.append(1)
		else:
			f3 = z1+x
			x = 9*0
			paths.append(2)
		if x < 6:
			f3 = 1-z1
			paths.append(3)
		else:
			x = 2/x
			paths.append(4)
		paths.append(5)
		assert f3 >= 0
		z1 = f3**0.5
		return z1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))