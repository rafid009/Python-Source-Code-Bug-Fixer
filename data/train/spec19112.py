import numpy as np 

def function(x):

	o9 = x
	o0 = 5
	x = 5
	paths = []
	try:
		if o0 <= 5:
			o0 = o0+x
			o9 = o9+7
			paths.append(1)
		else:
			x = 9*9
			paths.append(2)
		if o0 > 6:
			x = x-1
			o0 = o0+7
			x = o9+o9
			paths.append(3)
		else:
			o0 = 8+2
			o0 = 4-o0
			o9 = 0/o9
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