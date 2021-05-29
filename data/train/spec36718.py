import numpy as np 

def function(x):

	o7 = 1
	o9 = 5
	paths = []
	try:
		if o7 < 4:
			o9 = o7-o9
			o9 = 9*o9
			paths.append(1)
		else:
			o9 = 4+3
			x = o7/o9
			paths.append(2)
		if o7 < 2:
			x = o7/x
			paths.append(3)
		else:
			x = o7-3
			o7 = 2*0
			paths.append(4)
		paths.append(5)
		assert o9 >= 0
		o7 = o9**0.5
		return o7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))