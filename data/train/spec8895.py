import numpy as np 

def function(x):

	w1 = x
	k6 = 3
	paths = []
	try:
		if w1 >= 2:
			k6 = k6/2
			x = 9*4
			paths.append(1)
		else:
			w1 = w1-4
			paths.append(2)
		if k6 <= 0:
			w1 = 8-k6
			k6 = w1-9
			k6 = k6-k6
			paths.append(3)
		else:
			k6 = 2/9
			k6 = x+4
			paths.append(4)
		paths.append(5)
		assert w1 >= 0
		k6 = w1**0.5
		return k6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))