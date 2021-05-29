import numpy as np 

def function(x):

	w8 = 2
	u8 = 2
	paths = []
	try:
		if w8 <= 4:
			u8 = u8+x
			paths.append(1)
		else:
			w8 = 4+x
			paths.append(2)
		if w8 < 5:
			w8 = 2+x
			u8 = 1-u8
			w8 = 1-8
			paths.append(3)
		else:
			u8 = 0/7
			u8 = 4+4
			w8 = w8-9
			paths.append(4)
		paths.append(5)
		assert u8 >= 0
		w8 = u8**0.5
		return w8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))