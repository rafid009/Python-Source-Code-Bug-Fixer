import numpy as np 

def function(x):

	b9 = x
	w4 = x
	paths = []
	try:
		if w4 < 4:
			w4 = w4-7
			paths.append(1)
		else:
			w4 = w4+w4
			b9 = 9/9
			paths.append(2)
		if x > 4:
			x = x*b9
			x = x-x
			x = 3*8
			paths.append(3)
		else:
			w4 = 7+w4
			w4 = w4/7
			x = 2*b9
			paths.append(4)
		paths.append(5)
		assert w4 >= 0
		b9 = w4**0.5
		return b9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))