import numpy as np 

def function(x):

	a3 = x
	w6 = x
	x = 6
	paths = []
	try:
		if x < 6:
			a3 = 9+a3
			a3 = 7/5
			x = 4-a3
			paths.append(1)
		else:
			a3 = a3-6
			w6 = 8/3
			paths.append(2)
		if w6 > 6:
			a3 = a3/2
			x = 9/7
			x = x/x
			paths.append(3)
		else:
			x = x+7
			w6 = a3-w6
			paths.append(4)
		paths.append(5)
		assert w6 >= 0
		a3 = w6**0.5
		return a3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))