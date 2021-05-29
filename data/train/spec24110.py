import numpy as np 

def function(x):

	w8 = x
	f7 = x
	paths = []
	try:
		if x > 9:
			w8 = w8-0
			paths.append(1)
		else:
			w8 = 2+9
			paths.append(2)
		if w8 <= 2:
			w8 = w8-1
			paths.append(3)
		else:
			f7 = f7*w8
			paths.append(4)
		paths.append(5)
		assert f7 >= 0
		x = f7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))