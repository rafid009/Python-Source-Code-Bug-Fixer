import numpy as np 

def function(x):

	f1 = 8
	w7 = x
	paths = []
	try:
		if x >= 9:
			w7 = f1-w7
			paths.append(1)
		else:
			w7 = 5+9
			paths.append(2)
		if w7 >= 8:
			x = f1*0
			f1 = f1+5
			paths.append(3)
		else:
			w7 = w7*x
			paths.append(4)
		paths.append(5)
		assert w7 >= 0
		x = w7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))