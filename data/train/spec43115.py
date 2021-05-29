import numpy as np 

def function(x):

	v0 = x
	o9 = x
	x = 5
	paths = []
	try:
		if o9 < 5:
			v0 = 6*o9
			o9 = o9/3
			o9 = o9-6
			paths.append(1)
		else:
			v0 = o9+x
			x = 2/x
			paths.append(2)
		if x < 4:
			o9 = o9/4
			x = 1+2
			paths.append(3)
		else:
			o9 = 9/o9
			paths.append(4)
		paths.append(5)
		assert v0 >= 0
		o9 = v0**0.5
		return o9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))