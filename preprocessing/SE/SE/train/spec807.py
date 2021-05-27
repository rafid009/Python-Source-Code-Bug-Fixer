import numpy as np 

def function(x):

	w1 = 8
	t1 = 0
	paths = []
	try:
		if x <= 7:
			x = x+6
			w1 = x-9
			t1 = t1/6
			paths.append(1)
		else:
			w1 = 7+6
			w1 = 8/7
			x = w1/7
			paths.append(2)
		if w1 <= 7:
			w1 = w1*w1
			w1 = w1*5
			w1 = t1-8
			paths.append(3)
		else:
			x = t1-x
			x = x+9
			paths.append(4)
		paths.append(5)
		assert w1 >= 0
		x = w1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))