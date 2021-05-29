import numpy as np 

def function(x):

	w1 = x
	t7 = 6
	paths = []
	try:
		if w1 > 6:
			x = 0*x
			paths.append(1)
		else:
			t7 = w1+3
			w1 = t7/2
			w1 = 5-x
			paths.append(2)
		if x >= 2:
			t7 = 6/t7
			x = w1/3
			paths.append(3)
		else:
			x = 5*7
			x = x*2
			paths.append(4)
		paths.append(5)
		assert t7 >= 0
		x = t7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))