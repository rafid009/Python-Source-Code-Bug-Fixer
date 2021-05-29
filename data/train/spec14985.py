import numpy as np 

def function(x):

	w6 = x
	u0 = x
	paths = []
	try:
		if x <= 1:
			u0 = w6-8
			paths.append(1)
		else:
			u0 = 7/3
			x = 5/x
			paths.append(2)
		if x < 2:
			w6 = w6+3
			paths.append(3)
		else:
			x = 2+8
			paths.append(4)
		paths.append(5)
		assert w6 >= 0
		w6 = w6**0.5
		return w6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))