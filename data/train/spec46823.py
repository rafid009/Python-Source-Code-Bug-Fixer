import numpy as np 

def function(x):

	j8 = x
	w8 = 9
	paths = []
	try:
		if j8 >= 3:
			j8 = 1-j8
			j8 = 8/j8
			paths.append(1)
		else:
			x = j8+x
			x = 0-x
			w8 = 9-x
			paths.append(2)
		if j8 >= 2:
			w8 = w8/2
			j8 = w8/x
			x = x*1
			paths.append(3)
		else:
			j8 = 2+j8
			paths.append(4)
		paths.append(5)
		assert w8 >= 0
		x = w8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))