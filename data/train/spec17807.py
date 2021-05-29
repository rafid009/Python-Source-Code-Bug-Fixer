import numpy as np 

def function(x):

	e4 = x
	w5 = x
	paths = []
	try:
		if x >= 5:
			w5 = w5-9
			e4 = 9/e4
			paths.append(1)
		else:
			w5 = w5/1
			w5 = 2*w5
			w5 = e4+3
			paths.append(2)
		if e4 >= 4:
			x = 7+6
			paths.append(3)
		else:
			e4 = e4+6
			w5 = e4*2
			w5 = w5+w5
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