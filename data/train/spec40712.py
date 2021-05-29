import numpy as np 

def function(x):

	w1 = x
	j8 = x
	paths = []
	try:
		if w1 >= 4:
			w1 = j8-9
			j8 = 1-j8
			paths.append(1)
		else:
			j8 = j8-8
			paths.append(2)
		if j8 >= 4:
			x = x*1
			paths.append(3)
		else:
			w1 = w1/w1
			w1 = w1/1
			x = x+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))