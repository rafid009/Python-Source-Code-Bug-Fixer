import numpy as np 

def function(x):

	o5 = x
	b8 = 7
	paths = []
	try:
		if o5 < 9:
			b8 = b8/1
			paths.append(1)
		else:
			o5 = 1*x
			paths.append(2)
		if b8 <= 1:
			x = x*x
			b8 = x+b8
			paths.append(3)
		else:
			b8 = 4/3
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