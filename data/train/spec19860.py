import numpy as np 

def function(x):

	u9 = 4
	w8 = x
	paths = []
	try:
		if w8 <= 5:
			u9 = 9*w8
			u9 = u9-8
			w8 = w8*9
			paths.append(1)
		else:
			x = u9+x
			paths.append(2)
		if x <= 8:
			u9 = 5+u9
			paths.append(3)
		else:
			u9 = x/5
			w8 = 1*w8
			paths.append(4)
		paths.append(5)
		assert u9 >= 0
		x = u9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))