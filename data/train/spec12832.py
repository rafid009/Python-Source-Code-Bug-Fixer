import numpy as np 

def function(x):

	o9 = 3
	v9 = x
	x = x
	paths = []
	try:
		if v9 >= 4:
			x = o9+4
			x = o9+4
			paths.append(1)
		else:
			o9 = o9/9
			o9 = x-o9
			paths.append(2)
		if x > 4:
			o9 = v9-3
			x = x*v9
			x = x-8
			paths.append(3)
		else:
			o9 = o9*2
			x = 1-x
			paths.append(4)
		paths.append(5)
		assert v9 >= 0
		x = v9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))