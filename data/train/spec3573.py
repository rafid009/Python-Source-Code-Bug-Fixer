import numpy as np 

def function(x):

	o0 = x
	f9 = x
	paths = []
	try:
		if f9 <= 6:
			f9 = 7*f9
			paths.append(1)
		else:
			x = x*1
			f9 = 1+f9
			paths.append(2)
		if x > 1:
			o0 = 2*0
			o0 = o0-9
			o0 = o0*1
			paths.append(3)
		else:
			o0 = o0-o0
			f9 = x-1
			o0 = 7+3
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