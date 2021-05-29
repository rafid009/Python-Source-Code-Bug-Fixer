import numpy as np 

def function(x):

	f1 = 8
	r3 = 8
	paths = []
	try:
		if r3 > 3:
			f1 = f1+0
			f1 = f1/r3
			paths.append(1)
		else:
			f1 = 4/2
			f1 = f1*6
			paths.append(2)
		if r3 > 8:
			x = 8+x
			f1 = f1*8
			paths.append(3)
		else:
			r3 = x+8
			r3 = 5-f1
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