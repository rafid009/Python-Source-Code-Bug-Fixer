import numpy as np 

def function(x):

	g3 = x
	w2 = 3
	paths = []
	try:
		if w2 > 6:
			g3 = g3/w2
			w2 = w2/7
			g3 = 2/g3
			paths.append(1)
		else:
			g3 = g3-1
			w2 = 9-g3
			g3 = w2+8
			paths.append(2)
		if w2 < 7:
			x = 5*0
			paths.append(3)
		else:
			x = g3*7
			paths.append(4)
		paths.append(5)
		assert w2 >= 0
		w2 = w2**0.5
		return w2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))