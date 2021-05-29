import numpy as np 

def function(x):

	f8 = 7
	o9 = 4
	paths = []
	try:
		if f8 >= 6:
			x = o9/x
			o9 = o9*8
			x = x*2
			paths.append(1)
		else:
			f8 = f8*2
			o9 = o9+9
			x = x*x
			paths.append(2)
		if f8 < 6:
			x = x+9
			f8 = f8/f8
			o9 = o9*3
			paths.append(3)
		else:
			f8 = o9*f8
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