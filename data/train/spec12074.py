import numpy as np 

def function(x):

	b8 = x
	f1 = 1
	paths = []
	try:
		if b8 >= 5:
			x = 6/x
			f1 = 1-f1
			paths.append(1)
		else:
			x = x*4
			f1 = f1*8
			f1 = b8-f1
			paths.append(2)
		if b8 < 9:
			f1 = f1/9
			paths.append(3)
		else:
			x = 4-x
			x = 8*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b8 = x**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))