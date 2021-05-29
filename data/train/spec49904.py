import numpy as np 

def function(x):

	o9 = x
	w8 = 3
	paths = []
	try:
		if x >= 1:
			w8 = w8*8
			w8 = 2+2
			paths.append(1)
		else:
			x = w8*5
			paths.append(2)
		if o9 > 2:
			x = x*8
			w8 = 7*x
			w8 = w8-3
			paths.append(3)
		else:
			w8 = w8-9
			o9 = o9+1
			w8 = 9*w8
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