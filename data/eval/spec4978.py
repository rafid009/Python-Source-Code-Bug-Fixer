import numpy as np 

def function(x):

	i8 = x
	w5 = x
	paths = []
	try:
		if i8 >= 9:
			w5 = 9*1
			i8 = 1-w5
			w5 = x/1
			paths.append(1)
		else:
			i8 = 6*i8
			paths.append(2)
		if w5 >= 1:
			x = x*x
			paths.append(3)
		else:
			i8 = i8*8
			w5 = w5-7
			paths.append(4)
		paths.append(5)
		assert i8 >= 0
		x = i8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))