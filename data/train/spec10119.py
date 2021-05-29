import numpy as np 

def function(x):

	b0 = 9
	o5 = 6
	paths = []
	try:
		if o5 > 4:
			b0 = b0/o5
			b0 = b0*x
			o5 = 7-o5
			paths.append(1)
		else:
			x = 3-x
			b0 = 9-2
			paths.append(2)
		if x >= 7:
			b0 = b0*4
			paths.append(3)
		else:
			o5 = 1/7
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