import numpy as np 

def function(x):

	w2 = x
	y8 = x
	paths = []
	try:
		if x < 7:
			w2 = w2+0
			w2 = w2*3
			paths.append(1)
		else:
			x = 2-3
			x = x+x
			x = y8-0
			paths.append(2)
		if y8 < 7:
			x = 2+x
			x = 8*4
			paths.append(3)
		else:
			w2 = x+7
			y8 = 0/y8
			paths.append(4)
		paths.append(5)
		assert w2 >= 0
		x = w2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))