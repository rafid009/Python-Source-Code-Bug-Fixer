import numpy as np 

def function(x):

	w5 = 2
	j1 = x
	paths = []
	try:
		if j1 >= 9:
			x = x*4
			w5 = w5*5
			paths.append(1)
		else:
			x = j1*3
			paths.append(2)
		if w5 >= 3:
			w5 = 2*6
			w5 = x/9
			w5 = 0-w5
			paths.append(3)
		else:
			x = 2+6
			x = 2*5
			paths.append(4)
		paths.append(5)
		assert j1 >= 0
		w5 = j1**0.5
		return w5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))