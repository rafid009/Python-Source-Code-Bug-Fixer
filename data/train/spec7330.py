import numpy as np 

def function(x):

	g5 = x
	w8 = x
	paths = []
	try:
		if x >= 4:
			g5 = g5*w8
			w8 = w8/9
			g5 = g5/1
			paths.append(1)
		else:
			w8 = 7*w8
			g5 = g5+7
			paths.append(2)
		if w8 < 3:
			x = 9+g5
			g5 = 2*g5
			paths.append(3)
		else:
			g5 = g5*8
			g5 = x*2
			g5 = 7-g5
			paths.append(4)
		paths.append(5)
		assert g5 >= 0
		x = g5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))