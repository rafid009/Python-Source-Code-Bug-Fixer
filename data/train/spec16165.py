import numpy as np 

def function(x):

	j8 = 8
	w8 = x
	paths = []
	try:
		if w8 <= 1:
			w8 = w8*5
			x = 6*x
			w8 = 1-6
			paths.append(1)
		else:
			x = x/j8
			j8 = 0+5
			paths.append(2)
		if x < 2:
			w8 = 5/w8
			w8 = w8*3
			x = 4-7
			paths.append(3)
		else:
			j8 = 5+j8
			j8 = j8*7
			x = 3/4
			paths.append(4)
		paths.append(5)
		assert w8 >= 0
		w8 = w8**0.5
		return w8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))