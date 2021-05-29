import numpy as np 

def function(x):

	f1 = x
	o0 = 2
	paths = []
	try:
		if f1 >= 3:
			x = o0-o0
			x = x/f1
			o0 = 2+f1
			paths.append(1)
		else:
			x = f1*x
			o0 = f1*o0
			o0 = 3*4
			paths.append(2)
		if x < 9:
			o0 = o0+o0
			x = 8*f1
			o0 = o0/o0
			paths.append(3)
		else:
			o0 = o0-2
			x = x+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f1 = x**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))