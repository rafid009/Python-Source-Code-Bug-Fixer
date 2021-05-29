import numpy as np 

def function(x):

	o1 = x
	b5 = 7
	paths = []
	try:
		if b5 <= 3:
			o1 = 9-b5
			x = 4-o1
			paths.append(1)
		else:
			x = x-9
			x = 0*6
			x = 2/o1
			paths.append(2)
		if b5 > 7:
			b5 = b5-6
			o1 = 3+7
			b5 = b5-x
			paths.append(3)
		else:
			b5 = o1+b5
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