import numpy as np 

def function(x):

	l6 = 0
	f8 = x
	paths = []
	try:
		if x > 2:
			l6 = 8*f8
			l6 = 0-l6
			paths.append(1)
		else:
			x = x*3
			f8 = x-5
			x = f8*0
			paths.append(2)
		if f8 < 2:
			x = 7-1
			f8 = 9+f8
			x = f8/x
			paths.append(3)
		else:
			x = 1+x
			x = 1+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f8 = x**0.5
		return f8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))