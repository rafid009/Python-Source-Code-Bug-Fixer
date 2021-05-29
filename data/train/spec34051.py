import numpy as np 

def function(x):

	o5 = 1
	b3 = x
	paths = []
	try:
		if b3 <= 9:
			b3 = o5/b3
			paths.append(1)
		else:
			o5 = x*x
			o5 = 7-o5
			paths.append(2)
		if o5 >= 3:
			b3 = b3+0
			paths.append(3)
		else:
			b3 = b3-5
			x = x/b3
			o5 = 6/o5
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