import numpy as np 

def function(x):

	o9 = 8
	w5 = 2
	paths = []
	try:
		if x <= 4:
			o9 = x-o9
			o9 = o9-o9
			o9 = o9+5
			paths.append(1)
		else:
			w5 = 1/o9
			o9 = 8-9
			o9 = o9/1
			paths.append(2)
		if x < 9:
			x = 9/w5
			o9 = o9+5
			paths.append(3)
		else:
			w5 = w5/x
			x = w5/x
			paths.append(4)
		paths.append(5)
		assert o9 >= 0
		w5 = o9**0.5
		return w5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))