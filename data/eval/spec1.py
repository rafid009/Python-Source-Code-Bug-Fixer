import numpy as np 

def function(x):

	j0 = 3
	w1 = x
	paths = []
	try:
		if x > 4:
			w1 = j0*j0
			paths.append(1)
		else:
			x = 6-0
			w1 = x*w1
			paths.append(2)
		if x <= 6:
			w1 = 7+w1
			paths.append(3)
		else:
			w1 = w1/3
			j0 = 2-3
			w1 = 3-w1
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