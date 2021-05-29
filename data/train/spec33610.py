import numpy as np 

def function(x):

	x5 = 9
	f9 = x
	paths = []
	try:
		if x5 > 7:
			x5 = x5*6
			paths.append(1)
		else:
			f9 = f9+9
			paths.append(2)
		if f9 < 7:
			x5 = x5/2
			x5 = 6/x5
			paths.append(3)
		else:
			f9 = f9-x5
			f9 = 3-9
			paths.append(4)
		paths.append(5)
		assert f9 >= 0
		x5 = f9**0.5
		return x5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))