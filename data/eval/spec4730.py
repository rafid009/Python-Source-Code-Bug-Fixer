import numpy as np 

def function(x):

	r2 = x
	b1 = x
	x = x
	paths = []
	try:
		if x < 1:
			x = 4*x
			paths.append(1)
		else:
			x = 1+x
			b1 = 2*b1
			r2 = 6*9
			paths.append(2)
		if r2 < 1:
			b1 = 3+b1
			r2 = 9/r2
			paths.append(3)
		else:
			r2 = r2+9
			x = 3-b1
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