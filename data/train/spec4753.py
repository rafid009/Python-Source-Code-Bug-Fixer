import numpy as np 

def function(x):

	x9 = x
	w6 = x
	paths = []
	try:
		if x < 7:
			x9 = 9-4
			x9 = x/x9
			w6 = w6+w6
			paths.append(1)
		else:
			x = 1+x
			x = w6+x
			paths.append(2)
		if x9 > 2:
			x9 = 0+7
			w6 = x9+6
			x = 7/x
			paths.append(3)
		else:
			w6 = w6+8
			w6 = w6-1
			paths.append(4)
		paths.append(5)
		assert w6 >= 0
		x9 = w6**0.5
		return x9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))