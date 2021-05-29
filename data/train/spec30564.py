import numpy as np 

def function(x):

	a0 = 3
	f0 = x
	paths = []
	try:
		if a0 < 0:
			f0 = 5-8
			paths.append(1)
		else:
			x = x/8
			x = x+0
			paths.append(2)
		if a0 > 7:
			f0 = 0-8
			paths.append(3)
		else:
			f0 = f0-4
			paths.append(4)
		paths.append(5)
		assert f0 >= 0
		a0 = f0**0.5
		return a0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))