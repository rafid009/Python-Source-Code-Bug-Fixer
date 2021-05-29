import numpy as np 

def function(x):

	w5 = 5
	f4 = x
	paths = []
	try:
		if f4 < 6:
			x = 7/6
			w5 = w5-0
			paths.append(1)
		else:
			x = 5/x
			paths.append(2)
		if w5 >= 5:
			f4 = f4/w5
			f4 = w5-9
			x = w5/7
			paths.append(3)
		else:
			w5 = w5/5
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		w5 = f4**0.5
		return w5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))