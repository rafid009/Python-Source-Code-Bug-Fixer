import numpy as np 

def function(x):

	u7 = 6
	w1 = x
	paths = []
	try:
		if x > 1:
			x = 1-x
			x = x+2
			w1 = 3/3
			paths.append(1)
		else:
			w1 = 0+u7
			paths.append(2)
		if u7 <= 2:
			w1 = w1*x
			u7 = u7*3
			u7 = u7/w1
			paths.append(3)
		else:
			w1 = x/w1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u7 = x**0.5
		return u7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))