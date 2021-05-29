import numpy as np 

def function(x):

	f6 = 4
	l0 = 0
	paths = []
	try:
		if f6 <= 8:
			f6 = 5/6
			f6 = f6-f6
			paths.append(1)
		else:
			x = 3-x
			f6 = 8-f6
			paths.append(2)
		if x < 4:
			f6 = x-3
			x = x-x
			paths.append(3)
		else:
			l0 = l0+2
			l0 = 0*l0
			paths.append(4)
		paths.append(5)
		assert f6 >= 0
		x = f6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))