import numpy as np 

def function(x):

	w6 = x
	u4 = x
	paths = []
	try:
		if x < 6:
			u4 = 5+5
			x = 1*w6
			paths.append(1)
		else:
			w6 = u4/x
			x = w6*2
			paths.append(2)
		if w6 > 3:
			x = x-8
			u4 = 1+x
			paths.append(3)
		else:
			u4 = 3-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w6 = x**0.5
		return w6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))