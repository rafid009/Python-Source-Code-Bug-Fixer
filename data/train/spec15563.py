import numpy as np 

def function(x):

	v0 = x
	o9 = x
	paths = []
	try:
		if o9 >= 3:
			o9 = x/4
			o9 = o9+1
			paths.append(1)
		else:
			x = o9*x
			x = 9+x
			v0 = v0-o9
			paths.append(2)
		if o9 > 5:
			x = x+v0
			o9 = v0+6
			paths.append(3)
		else:
			x = 7*5
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