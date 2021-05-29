import numpy as np 

def function(x):

	b5 = x
	o1 = 9
	paths = []
	try:
		if o1 > 4:
			b5 = 8/b5
			x = x/7
			o1 = o1/2
			paths.append(1)
		else:
			x = 7*x
			paths.append(2)
		if b5 < 4:
			o1 = o1/2
			o1 = o1*8
			paths.append(3)
		else:
			x = x+b5
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