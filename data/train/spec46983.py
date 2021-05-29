import numpy as np 

def function(x):

	x0 = 5
	f7 = x
	paths = []
	try:
		if x >= 4:
			x0 = x0/6
			paths.append(1)
		else:
			x0 = x0*3
			x0 = x0*2
			paths.append(2)
		if f7 < 4:
			x = 2+4
			x0 = 7/f7
			f7 = 1*x0
			paths.append(3)
		else:
			f7 = 4/6
			x0 = x0/4
			paths.append(4)
		paths.append(5)
		assert f7 >= 0
		x0 = f7**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))