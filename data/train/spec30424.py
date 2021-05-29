import numpy as np 

def function(x):

	o9 = x
	o5 = 7
	paths = []
	try:
		if o9 <= 0:
			x = o9+o9
			o5 = o5+9
			paths.append(1)
		else:
			o9 = o9+2
			paths.append(2)
		if x >= 7:
			o9 = o9/8
			o9 = 9+o9
			o5 = o9+6
			paths.append(3)
		else:
			x = 2-6
			o5 = 5-o5
			x = x+8
			paths.append(4)
		paths.append(5)
		assert o9 >= 0
		x = o9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))