import numpy as np 

def function(x):

	f4 = x
	a3 = 6
	paths = []
	try:
		if x >= 9:
			x = x*6
			x = 8*x
			f4 = f4+f4
			paths.append(1)
		else:
			f4 = a3*7
			a3 = a3/a3
			paths.append(2)
		if f4 < 7:
			x = x/a3
			paths.append(3)
		else:
			a3 = x+a3
			f4 = 9*1
			a3 = 0+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))