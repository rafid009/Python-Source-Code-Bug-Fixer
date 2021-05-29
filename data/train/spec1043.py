import numpy as np 

def function(x):

	w3 = x
	u4 = 0
	paths = []
	try:
		if u4 >= 3:
			x = w3*7
			u4 = u4/u4
			u4 = u4-u4
			paths.append(1)
		else:
			w3 = w3+8
			u4 = u4+9
			paths.append(2)
		if u4 < 2:
			x = 5*w3
			u4 = u4+0
			paths.append(3)
		else:
			x = 7+x
			w3 = 0+7
			x = u4-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w3 = x**0.5
		return w3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))