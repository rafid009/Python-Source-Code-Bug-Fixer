import numpy as np 

def function(x):

	u8 = x
	w7 = 3
	paths = []
	try:
		if x >= 6:
			u8 = 7/x
			paths.append(1)
		else:
			x = x-7
			w7 = w7/7
			x = x+w7
			paths.append(2)
		if u8 <= 3:
			x = w7*2
			x = x/x
			x = 1+u8
			paths.append(3)
		else:
			w7 = 6/w7
			u8 = w7/1
			w7 = w7+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w7 = x**0.5
		return w7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))