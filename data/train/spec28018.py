import numpy as np 

def function(x):

	b7 = 4
	o1 = x
	paths = []
	try:
		if o1 >= 5:
			b7 = b7-7
			paths.append(1)
		else:
			b7 = 2+b7
			o1 = o1-2
			b7 = 3*b7
			paths.append(2)
		if x > 0:
			b7 = b7/6
			x = x-x
			paths.append(3)
		else:
			b7 = 3*x
			o1 = o1+3
			b7 = 6+x
			paths.append(4)
		paths.append(5)
		assert o1 >= 0
		x = o1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))