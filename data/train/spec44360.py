import numpy as np 

def function(x):

	r2 = 1
	y1 = x
	x = 0
	paths = []
	try:
		if y1 >= 3:
			r2 = r2/6
			r2 = r2+x
			paths.append(1)
		else:
			x = 1+y1
			paths.append(2)
		if y1 > 2:
			x = x*x
			x = 3*8
			x = 2*9
			paths.append(3)
		else:
			r2 = y1*r2
			r2 = 9*r2
			paths.append(4)
		paths.append(5)
		assert y1 >= 0
		x = y1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))