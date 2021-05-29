import numpy as np 

def function(x):

	w1 = 5
	j3 = x
	paths = []
	try:
		if w1 < 8:
			j3 = 8/j3
			j3 = 5-w1
			j3 = x-j3
			paths.append(1)
		else:
			x = x*w1
			x = w1+8
			paths.append(2)
		if w1 < 4:
			w1 = w1-8
			paths.append(3)
		else:
			j3 = 3*2
			j3 = 8+2
			w1 = 9-j3
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