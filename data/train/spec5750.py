import numpy as np 

def function(x):

	o0 = 4
	f0 = 7
	paths = []
	try:
		if f0 <= 9:
			o0 = 0-o0
			f0 = f0*3
			paths.append(1)
		else:
			x = f0+o0
			x = x-2
			o0 = o0*o0
			paths.append(2)
		if f0 < 1:
			x = 8*0
			x = x/4
			paths.append(3)
		else:
			f0 = f0-f0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o0 = x**0.5
		return o0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))