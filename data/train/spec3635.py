import numpy as np 

def function(x):

	o0 = x
	f9 = x
	paths = []
	try:
		if x <= 3:
			x = x/f9
			x = x-2
			o0 = o0+f9
			paths.append(1)
		else:
			f9 = x+8
			f9 = f9-7
			paths.append(2)
		if f9 <= 9:
			o0 = 3+7
			f9 = x+0
			f9 = f9+o0
			paths.append(3)
		else:
			o0 = 9-o0
			x = 7-9
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