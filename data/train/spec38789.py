import numpy as np 

def function(x):

	w5 = 1
	y8 = x
	paths = []
	try:
		if y8 <= 8:
			x = 3*9
			y8 = w5+y8
			x = x+6
			paths.append(1)
		else:
			w5 = w5*w5
			y8 = 4/x
			x = 5-9
			paths.append(2)
		if x < 5:
			x = x+y8
			paths.append(3)
		else:
			w5 = 5/2
			paths.append(4)
		paths.append(5)
		assert y8 >= 0
		w5 = y8**0.5
		return w5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))