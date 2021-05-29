import numpy as np 

def function(x):

	w7 = x
	y8 = x
	paths = []
	try:
		if y8 <= 5:
			x = w7+0
			paths.append(1)
		else:
			w7 = w7/x
			paths.append(2)
		if w7 > 4:
			w7 = x*w7
			paths.append(3)
		else:
			y8 = y8*1
			x = x-x
			w7 = 5*w7
			paths.append(4)
		paths.append(5)
		assert y8 >= 0
		w7 = y8**0.5
		return w7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))