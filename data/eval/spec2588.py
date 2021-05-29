import numpy as np 

def function(x):

	w2 = 8
	v4 = 7
	paths = []
	try:
		if x < 0:
			v4 = 1*3
			v4 = w2/6
			paths.append(1)
		else:
			v4 = x-x
			v4 = 3/w2
			w2 = w2-9
			paths.append(2)
		if w2 > 0:
			w2 = w2+2
			w2 = 6*w2
			x = 7-x
			paths.append(3)
		else:
			v4 = v4/w2
			w2 = w2-2
			paths.append(4)
		paths.append(5)
		assert v4 >= 0
		w2 = v4**0.5
		return w2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))