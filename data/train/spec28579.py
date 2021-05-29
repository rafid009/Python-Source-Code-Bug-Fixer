import numpy as np 

def function(x):

	f9 = 3
	l0 = 7
	paths = []
	try:
		if x >= 1:
			x = 9/x
			x = x-x
			l0 = 5*3
			paths.append(1)
		else:
			f9 = 0-f9
			f9 = 4-0
			paths.append(2)
		if l0 >= 4:
			f9 = 2-f9
			paths.append(3)
		else:
			l0 = 8*8
			paths.append(4)
		paths.append(5)
		assert f9 >= 0
		x = f9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))