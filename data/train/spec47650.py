import numpy as np 

def function(x):

	w6 = 2
	f1 = x
	paths = []
	try:
		if f1 < 0:
			f1 = x+f1
			f1 = f1-2
			w6 = f1*w6
			paths.append(1)
		else:
			f1 = w6*7
			w6 = w6*w6
			f1 = 5*x
			paths.append(2)
		if w6 <= 3:
			w6 = 5*w6
			x = x*6
			x = x-x
			paths.append(3)
		else:
			f1 = 4+x
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