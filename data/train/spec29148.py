import numpy as np 

def function(x):

	w2 = x
	y4 = 3
	paths = []
	try:
		if y4 <= 1:
			w2 = 1*w2
			paths.append(1)
		else:
			x = 5/6
			paths.append(2)
		if w2 <= 3:
			y4 = w2+2
			paths.append(3)
		else:
			w2 = w2-w2
			w2 = 1+y4
			paths.append(4)
		paths.append(5)
		assert w2 >= 0
		y4 = w2**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))