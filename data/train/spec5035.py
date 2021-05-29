import numpy as np 

def function(x):

	w5 = 9
	w7 = 4
	paths = []
	try:
		if w5 > 5:
			x = 6*x
			paths.append(1)
		else:
			w7 = w7-7
			w5 = 4-w5
			paths.append(2)
		if w7 <= 8:
			w5 = x/9
			paths.append(3)
		else:
			w5 = 4*9
			x = x/1
			w5 = w5+5
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