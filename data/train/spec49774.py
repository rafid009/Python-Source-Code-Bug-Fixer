import numpy as np 

def function(x):

	o2 = x
	x8 = 2
	paths = []
	try:
		if o2 >= 6:
			o2 = x8*2
			x = x*7
			x8 = x8*x
			paths.append(1)
		else:
			x = 3+x
			x = 1+x
			paths.append(2)
		if o2 <= 6:
			x = x+x8
			paths.append(3)
		else:
			x8 = 7+x8
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		x = o2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))