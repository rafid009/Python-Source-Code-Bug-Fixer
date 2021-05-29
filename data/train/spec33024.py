import numpy as np 

def function(x):

	f0 = 8
	j1 = x
	paths = []
	try:
		if f0 > 2:
			x = f0/x
			f0 = 9*f0
			paths.append(1)
		else:
			x = x*7
			f0 = 5*f0
			paths.append(2)
		if j1 >= 6:
			x = j1/x
			f0 = f0+9
			f0 = f0-5
			paths.append(3)
		else:
			j1 = j1-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f0 = x**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))