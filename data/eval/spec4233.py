import numpy as np 

def function(x):

	o9 = x
	b9 = 7
	paths = []
	try:
		if x >= 1:
			b9 = o9-b9
			b9 = b9-4
			paths.append(1)
		else:
			b9 = o9*2
			paths.append(2)
		if o9 >= 8:
			x = x-x
			paths.append(3)
		else:
			o9 = o9/1
			paths.append(4)
		paths.append(5)
		assert o9 >= 0
		o9 = o9**0.5
		return o9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))