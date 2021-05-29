import numpy as np 

def function(x):

	w5 = 2
	j4 = x
	paths = []
	try:
		if x >= 2:
			j4 = x+4
			x = 0+6
			w5 = 6/j4
			paths.append(1)
		else:
			x = 0+5
			w5 = w5-7
			paths.append(2)
		if x <= 1:
			w5 = 7*j4
			w5 = 2+0
			paths.append(3)
		else:
			x = 2/x
			j4 = j4*7
			x = x-6
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