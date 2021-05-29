import numpy as np 

def function(x):

	w8 = x
	g5 = x
	paths = []
	try:
		if g5 > 6:
			x = x/w8
			w8 = x*w8
			paths.append(1)
		else:
			g5 = 9-6
			g5 = g5+7
			paths.append(2)
		if x <= 7:
			g5 = g5-4
			g5 = 9/7
			paths.append(3)
		else:
			x = 5-x
			g5 = 9/g5
			g5 = g5-x
			paths.append(4)
		paths.append(5)
		assert w8 >= 0
		w8 = w8**0.5
		return w8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))