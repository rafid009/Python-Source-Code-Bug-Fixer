import numpy as np 

def function(x):

	b1 = 8
	f2 = x
	paths = []
	try:
		if x >= 6:
			b1 = b1*3
			b1 = 5*b1
			paths.append(1)
		else:
			b1 = b1+x
			x = 2-x
			paths.append(2)
		if b1 >= 6:
			f2 = 6/9
			x = x-2
			f2 = 0*f2
			paths.append(3)
		else:
			f2 = f2/f2
			x = x+8
			paths.append(4)
		paths.append(5)
		assert b1 >= 0
		x = b1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))