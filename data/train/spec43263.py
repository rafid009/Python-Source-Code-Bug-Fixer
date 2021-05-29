import numpy as np 

def function(x):

	o1 = x
	b3 = 0
	paths = []
	try:
		if b3 >= 0:
			o1 = o1/8
			b3 = 9*8
			x = 1/x
			paths.append(1)
		else:
			x = o1+1
			b3 = 1+b3
			paths.append(2)
		if x <= 2:
			b3 = o1/9
			o1 = 3-o1
			paths.append(3)
		else:
			o1 = o1-b3
			b3 = b3*o1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o1 = x**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))