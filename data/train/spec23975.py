import numpy as np 

def function(x):

	x6 = 9
	w6 = x
	paths = []
	try:
		if w6 >= 3:
			x = 9+x
			w6 = w6-8
			w6 = w6-w6
			paths.append(1)
		else:
			w6 = w6+3
			x6 = 9/8
			paths.append(2)
		if x6 <= 5:
			x = x+7
			paths.append(3)
		else:
			w6 = 7-x
			w6 = w6*w6
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