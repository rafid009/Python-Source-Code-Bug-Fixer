import numpy as np 

def function(x):

	w4 = x
	i9 = 3
	x = x
	paths = []
	try:
		if w4 < 1:
			w4 = 1-6
			w4 = w4*0
			paths.append(1)
		else:
			i9 = i9-9
			i9 = i9+w4
			w4 = x+w4
			paths.append(2)
		if i9 >= 2:
			w4 = w4+0
			i9 = i9/8
			paths.append(3)
		else:
			x = x-i9
			x = w4/x
			w4 = 5-7
			paths.append(4)
		paths.append(5)
		assert i9 >= 0
		x = i9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))