import numpy as np 

def function(x):

	f0 = 3
	f2 = x
	paths = []
	try:
		if f2 <= 7:
			f2 = 7*3
			paths.append(1)
		else:
			x = 0-x
			x = 0*5
			paths.append(2)
		if f0 < 0:
			x = 2+f2
			paths.append(3)
		else:
			f0 = f0-0
			f0 = f0-x
			x = x*x
			paths.append(4)
		paths.append(5)
		assert f0 >= 0
		x = f0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))