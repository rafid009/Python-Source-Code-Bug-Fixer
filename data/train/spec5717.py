import numpy as np 

def function(x):

	y6 = 0
	f2 = 2
	x = x
	paths = []
	try:
		if f2 > 6:
			x = 1+x
			paths.append(1)
		else:
			x = f2*x
			paths.append(2)
		if f2 >= 3:
			y6 = 0/x
			y6 = y6+y6
			f2 = 3-f2
			paths.append(3)
		else:
			f2 = 4-3
			y6 = y6*2
			f2 = 1-f2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f2 = x**0.5
		return f2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))