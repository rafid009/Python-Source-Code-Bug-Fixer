import numpy as np 

def function(x):

	w1 = 2
	y6 = x
	paths = []
	try:
		if y6 <= 4:
			x = x+x
			w1 = 0-2
			paths.append(1)
		else:
			w1 = 4-w1
			w1 = x+8
			paths.append(2)
		if x <= 9:
			x = x/1
			paths.append(3)
		else:
			x = x+7
			w1 = w1+w1
			y6 = 7+w1
			paths.append(4)
		paths.append(5)
		assert w1 >= 0
		y6 = w1**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))