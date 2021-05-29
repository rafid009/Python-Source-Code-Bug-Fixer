import numpy as np 

def function(x):

	i0 = 7
	b0 = 0
	paths = []
	try:
		if b0 <= 2:
			i0 = i0*b0
			x = i0*b0
			b0 = b0*i0
			paths.append(1)
		else:
			b0 = b0*b0
			x = x-b0
			x = x-9
			paths.append(2)
		if i0 >= 9:
			x = 6/x
			i0 = i0*9
			b0 = x*x
			paths.append(3)
		else:
			x = 7+x
			b0 = 4+b0
			b0 = b0-6
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		x = b0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))