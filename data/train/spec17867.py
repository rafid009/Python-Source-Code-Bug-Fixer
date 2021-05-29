import numpy as np 

def function(x):

	e8 = x
	w5 = 0
	paths = []
	try:
		if e8 >= 7:
			x = 9+x
			w5 = 3+w5
			paths.append(1)
		else:
			e8 = e8+8
			e8 = 4/9
			paths.append(2)
		if e8 >= 6:
			e8 = w5/x
			e8 = x-x
			paths.append(3)
		else:
			e8 = e8/7
			w5 = w5-e8
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