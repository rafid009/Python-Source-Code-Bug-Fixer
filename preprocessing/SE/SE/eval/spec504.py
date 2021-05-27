import numpy as np 

def function(x):

	u1 = x
	w6 = x
	paths = []
	try:
		if x < 6:
			u1 = 7/u1
			u1 = u1-3
			paths.append(1)
		else:
			w6 = 8*w6
			u1 = x-u1
			x = w6+8
			paths.append(2)
		if w6 <= 7:
			u1 = u1-6
			paths.append(3)
		else:
			u1 = 8+u1
			paths.append(4)
		paths.append(5)
		assert u1 >= 0
		w6 = u1**0.5
		return w6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))