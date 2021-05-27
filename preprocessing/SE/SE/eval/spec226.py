import numpy as np 

def function(x):

	o9 = 9
	r9 = x
	paths = []
	try:
		if o9 > 4:
			x = x/6
			o9 = o9+9
			x = x/x
			paths.append(1)
		else:
			o9 = o9-2
			paths.append(2)
		if o9 < 3:
			o9 = o9+7
			o9 = o9/2
			x = x+9
			paths.append(3)
		else:
			o9 = o9*o9
			o9 = 1-x
			paths.append(4)
		paths.append(5)
		assert r9 >= 0
		x = r9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))