import numpy as np 

def function(x):

	o9 = 0
	v9 = 5
	paths = []
	try:
		if x <= 3:
			o9 = v9-o9
			paths.append(1)
		else:
			x = 4-o9
			o9 = o9*x
			x = x+1
			paths.append(2)
		if o9 <= 7:
			o9 = v9/v9
			paths.append(3)
		else:
			o9 = 7*o9
			v9 = v9/1
			x = o9/2
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