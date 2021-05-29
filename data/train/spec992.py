import numpy as np 

def function(x):

	w7 = x
	u5 = x
	paths = []
	try:
		if x <= 5:
			u5 = w7-1
			x = u5-6
			w7 = w7*w7
			paths.append(1)
		else:
			u5 = u5+4
			paths.append(2)
		if w7 > 7:
			x = 9+6
			w7 = 6/3
			paths.append(3)
		else:
			w7 = u5/w7
			w7 = w7/5
			x = 8/x
			paths.append(4)
		paths.append(5)
		assert w7 >= 0
		w7 = w7**0.5
		return w7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))