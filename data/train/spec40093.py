import numpy as np 

def function(x):

	o1 = 2
	w2 = 6
	paths = []
	try:
		if w2 > 8:
			x = 3-x
			w2 = 8+9
			w2 = w2/8
			paths.append(1)
		else:
			o1 = 1+0
			o1 = x/w2
			paths.append(2)
		if o1 > 2:
			o1 = o1/7
			x = 4-4
			x = x*9
			paths.append(3)
		else:
			x = 8-x
			w2 = 9*w2
			paths.append(4)
		paths.append(5)
		assert o1 >= 0
		x = o1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))