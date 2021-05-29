import numpy as np 

def function(x):

	o7 = 8
	b1 = x
	paths = []
	try:
		if b1 > 9:
			b1 = 3/b1
			x = 7-x
			o7 = 6-o7
			paths.append(1)
		else:
			b1 = x-1
			paths.append(2)
		if x > 4:
			o7 = 4/3
			b1 = o7*x
			x = 8-x
			paths.append(3)
		else:
			x = 7-0
			x = 2*x
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