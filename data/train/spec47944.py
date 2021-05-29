import numpy as np 

def function(x):

	w1 = x
	f6 = 6
	paths = []
	try:
		if x >= 9:
			w1 = w1-x
			paths.append(1)
		else:
			f6 = w1/1
			paths.append(2)
		if w1 > 9:
			f6 = f6-6
			x = 5-x
			w1 = 2/w1
			paths.append(3)
		else:
			f6 = 0+4
			f6 = w1-7
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