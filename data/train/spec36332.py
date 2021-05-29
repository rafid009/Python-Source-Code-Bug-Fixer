import numpy as np 

def function(x):

	o0 = x
	b1 = x
	x = x
	paths = []
	try:
		if x <= 0:
			x = x/x
			o0 = 2+o0
			o0 = o0+0
			paths.append(1)
		else:
			b1 = b1+7
			paths.append(2)
		if b1 <= 6:
			o0 = 6/o0
			o0 = o0-3
			x = 1-9
			paths.append(3)
		else:
			x = x*9
			b1 = 3*b1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b1 = x**0.5
		return b1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))