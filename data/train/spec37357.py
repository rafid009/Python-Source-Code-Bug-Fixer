import numpy as np 

def function(x):

	a9 = 6
	f4 = 4
	paths = []
	try:
		if f4 <= 4:
			f4 = 2+4
			x = 8*x
			paths.append(1)
		else:
			a9 = x+a9
			f4 = x*f4
			paths.append(2)
		if a9 < 2:
			f4 = f4*7
			paths.append(3)
		else:
			x = x-8
			f4 = f4/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f4 = x**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))