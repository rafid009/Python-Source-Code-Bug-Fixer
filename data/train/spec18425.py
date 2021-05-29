import numpy as np 

def function(x):

	f6 = x
	g0 = 0
	paths = []
	try:
		if x >= 4:
			g0 = f6-g0
			f6 = f6*7
			f6 = f6*x
			paths.append(1)
		else:
			f6 = f6-6
			f6 = f6+9
			paths.append(2)
		if g0 >= 8:
			g0 = 2/g0
			g0 = g0+x
			x = 5-4
			paths.append(3)
		else:
			f6 = 0+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f6 = x**0.5
		return f6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))