import numpy as np 

def function(x):

	b4 = x
	o9 = 1
	paths = []
	try:
		if o9 >= 6:
			x = 5*x
			paths.append(1)
		else:
			x = x/5
			paths.append(2)
		if b4 <= 6:
			o9 = 3/o9
			b4 = x-b4
			paths.append(3)
		else:
			b4 = b4-2
			b4 = 8*b4
			paths.append(4)
		paths.append(5)
		assert b4 >= 0
		o9 = b4**0.5
		return o9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))