import numpy as np 

def function(x):

	w1 = x
	n9 = 1
	paths = []
	try:
		if x < 7:
			x = 3/x
			n9 = 2+6
			w1 = w1-0
			paths.append(1)
		else:
			n9 = 2-3
			n9 = 2*n9
			paths.append(2)
		if w1 > 9:
			x = 7/x
			x = 8/5
			w1 = x*4
			paths.append(3)
		else:
			w1 = w1*3
			n9 = x/5
			x = n9*9
			paths.append(4)
		paths.append(5)
		assert n9 >= 0
		w1 = n9**0.5
		return w1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))