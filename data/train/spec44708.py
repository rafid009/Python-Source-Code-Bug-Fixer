import numpy as np 

def function(x):

	b0 = x
	o8 = x
	x = 1
	paths = []
	try:
		if o8 >= 9:
			b0 = b0+b0
			x = 9/b0
			x = 2/x
			paths.append(1)
		else:
			b0 = b0/8
			paths.append(2)
		if b0 > 6:
			o8 = 6-3
			o8 = 1-b0
			paths.append(3)
		else:
			b0 = b0*0
			b0 = o8+b0
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		b0 = b0**0.5
		return b0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))