import numpy as np 

def function(x):

	w6 = x
	y5 = x
	paths = []
	try:
		if w6 >= 3:
			y5 = y5+1
			w6 = w6/w6
			w6 = y5*1
			paths.append(1)
		else:
			x = x-1
			paths.append(2)
		if x >= 7:
			x = w6+3
			y5 = 7+y5
			y5 = 1-y5
			paths.append(3)
		else:
			w6 = w6*9
			x = x/3
			paths.append(4)
		paths.append(5)
		assert w6 >= 0
		w6 = w6**0.5
		return w6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))