import numpy as np 

def function(x):

	o5 = x
	b5 = 1
	paths = []
	try:
		if b5 <= 1:
			x = x/1
			o5 = 1*o5
			o5 = o5*o5
			paths.append(1)
		else:
			o5 = 8*o5
			o5 = o5-b5
			b5 = 4/b5
			paths.append(2)
		if o5 < 3:
			o5 = 4-b5
			b5 = 3*x
			paths.append(3)
		else:
			b5 = 2/b5
			b5 = 6*o5
			o5 = o5/o5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o5 = x**0.5
		return o5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))