import numpy as np 

def function(x):

	g8 = x
	w5 = x
	paths = []
	try:
		if x <= 6:
			w5 = x/w5
			paths.append(1)
		else:
			w5 = x+w5
			g8 = w5*1
			paths.append(2)
		if g8 < 5:
			x = 4-x
			g8 = 0+9
			paths.append(3)
		else:
			w5 = 0-w5
			x = 7/x
			w5 = w5-x
			paths.append(4)
		paths.append(5)
		assert w5 >= 0
		w5 = w5**0.5
		return w5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))