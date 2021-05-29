import numpy as np 

def function(x):

	o8 = 9
	b6 = 1
	paths = []
	try:
		if o8 > 1:
			b6 = 7+b6
			o8 = b6*o8
			o8 = o8-o8
			paths.append(1)
		else:
			x = 5-3
			paths.append(2)
		if b6 >= 9:
			b6 = b6*6
			b6 = 2+b6
			b6 = b6/9
			paths.append(3)
		else:
			x = o8+x
			b6 = 4*b6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b6 = x**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))