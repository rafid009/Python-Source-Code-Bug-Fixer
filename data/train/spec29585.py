import numpy as np 

def function(x):

	w6 = 1
	n3 = x
	paths = []
	try:
		if x <= 0:
			n3 = w6*n3
			paths.append(1)
		else:
			n3 = n3+0
			w6 = w6*1
			paths.append(2)
		if x > 2:
			n3 = n3-5
			n3 = 3/1
			w6 = 0+6
			paths.append(3)
		else:
			x = x/5
			n3 = n3+x
			n3 = 7/9
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