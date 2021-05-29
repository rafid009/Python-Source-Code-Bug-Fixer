import numpy as np 

def function(x):

	w8 = 9
	t5 = 0
	x = 2
	paths = []
	try:
		if w8 <= 9:
			w8 = w8*1
			w8 = w8/w8
			w8 = w8-9
			paths.append(1)
		else:
			x = x/x
			x = w8/9
			w8 = w8*1
			paths.append(2)
		if t5 <= 2:
			w8 = w8+4
			paths.append(3)
		else:
			t5 = t5-t5
			paths.append(4)
		paths.append(5)
		assert w8 >= 0
		x = w8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))