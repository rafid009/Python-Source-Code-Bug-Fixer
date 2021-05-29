import numpy as np 

def function(x):

	b9 = 0
	o9 = 7
	paths = []
	try:
		if b9 < 1:
			b9 = x-o9
			paths.append(1)
		else:
			x = x/9
			paths.append(2)
		if o9 >= 5:
			b9 = b9/3
			o9 = 3-o9
			b9 = b9+6
			paths.append(3)
		else:
			b9 = b9/b9
			o9 = o9+0
			x = 4+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o9 = x**0.5
		return o9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))