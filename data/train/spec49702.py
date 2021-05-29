import numpy as np 

def function(x):

	w6 = x
	x7 = 7
	paths = []
	try:
		if x7 <= 9:
			x7 = 9-x7
			x7 = w6+x
			x7 = 8-x
			paths.append(1)
		else:
			x7 = x7/7
			x7 = w6-1
			x7 = x7*0
			paths.append(2)
		if x7 <= 0:
			x = x*x7
			x = 1/8
			paths.append(3)
		else:
			w6 = w6-x7
			paths.append(4)
		paths.append(5)
		assert w6 >= 0
		x = w6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))