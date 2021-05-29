import numpy as np 

def function(x):

	u7 = x
	w1 = 0
	paths = []
	try:
		if x > 7:
			x = 1/u7
			paths.append(1)
		else:
			w1 = w1-5
			x = 6+x
			u7 = u7*w1
			paths.append(2)
		if w1 < 2:
			w1 = 0+7
			w1 = w1+5
			paths.append(3)
		else:
			w1 = x+9
			u7 = u7/x
			w1 = w1/8
			paths.append(4)
		paths.append(5)
		assert u7 >= 0
		w1 = u7**0.5
		return w1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))