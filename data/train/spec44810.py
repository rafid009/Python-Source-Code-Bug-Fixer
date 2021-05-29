import numpy as np 

def function(x):

	w7 = x
	u4 = 6
	paths = []
	try:
		if u4 <= 2:
			w7 = w7*2
			x = u4*x
			paths.append(1)
		else:
			u4 = 8*w7
			paths.append(2)
		if w7 <= 8:
			x = w7+x
			w7 = 3-w7
			u4 = u4+w7
			paths.append(3)
		else:
			w7 = w7-0
			paths.append(4)
		paths.append(5)
		assert u4 >= 0
		u4 = u4**0.5
		return u4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))