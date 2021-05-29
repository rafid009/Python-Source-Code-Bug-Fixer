import numpy as np 

def function(x):

	w5 = x
	y3 = 9
	paths = []
	try:
		if w5 >= 8:
			x = 8*w5
			paths.append(1)
		else:
			w5 = w5-5
			y3 = y3-5
			paths.append(2)
		if x > 0:
			x = x/w5
			y3 = y3/1
			paths.append(3)
		else:
			w5 = w5+7
			x = x+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y3 = x**0.5
		return y3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))