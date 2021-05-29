import numpy as np 

def function(x):

	h7 = x
	b7 = x
	x = x
	paths = []
	try:
		if x > 5:
			b7 = 5/b7
			x = x*h7
			paths.append(1)
		else:
			b7 = b7+0
			b7 = b7/8
			x = x/b7
			paths.append(2)
		if b7 >= 7:
			x = b7+b7
			x = x/x
			b7 = b7-9
			paths.append(3)
		else:
			b7 = b7+6
			x = b7-x
			h7 = x/h7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b7 = x**0.5
		return b7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))