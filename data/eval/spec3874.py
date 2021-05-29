import numpy as np 

def function(x):

	w1 = x
	w6 = x
	paths = []
	try:
		if w1 <= 3:
			x = x*1
			paths.append(1)
		else:
			w1 = w1-w6
			w6 = 7-w1
			paths.append(2)
		if w6 >= 2:
			w6 = w6/4
			w1 = 5-x
			paths.append(3)
		else:
			x = w6-2
			w6 = x+9
			w6 = w1-w6
			paths.append(4)
		paths.append(5)
		assert w1 >= 0
		w1 = w1**0.5
		return w1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))