import numpy as np 

def function(x):

	a1 = 2
	f0 = x
	paths = []
	try:
		if f0 > 0:
			a1 = f0/a1
			paths.append(1)
		else:
			x = 6*x
			x = x/f0
			paths.append(2)
		if x < 8:
			x = 2/f0
			paths.append(3)
		else:
			a1 = 6+4
			f0 = f0/x
			paths.append(4)
		paths.append(5)
		assert f0 >= 0
		a1 = f0**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))