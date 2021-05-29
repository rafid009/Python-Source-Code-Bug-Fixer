import numpy as np 

def function(x):

	r2 = 0
	f8 = 8
	paths = []
	try:
		if f8 < 1:
			x = x/r2
			f8 = f8+0
			paths.append(1)
		else:
			r2 = r2+1
			paths.append(2)
		if f8 >= 1:
			f8 = 5+f8
			r2 = f8+2
			paths.append(3)
		else:
			f8 = f8+f8
			r2 = x/x
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