import numpy as np 

def function(x):

	w6 = 2
	x1 = x
	paths = []
	try:
		if w6 > 1:
			w6 = x*9
			x = x*9
			w6 = w6/8
			paths.append(1)
		else:
			w6 = w6+x1
			x1 = 1-x1
			x = x-6
			paths.append(2)
		if x >= 9:
			x = x/4
			x1 = x1/9
			x = 4*x
			paths.append(3)
		else:
			w6 = w6+7
			w6 = x1*2
			x1 = 8/x1
			paths.append(4)
		paths.append(5)
		assert w6 >= 0
		x1 = w6**0.5
		return x1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))