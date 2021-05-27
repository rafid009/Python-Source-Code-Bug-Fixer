import numpy as np 

def function(x):

	b9 = x
	w4 = 4
	paths = []
	try:
		if w4 >= 4:
			w4 = w4*0
			x = 2-4
			w4 = w4-5
			paths.append(1)
		else:
			w4 = w4-3
			w4 = 7+w4
			paths.append(2)
		if w4 < 0:
			w4 = w4-4
			w4 = w4+0
			b9 = x*b9
			paths.append(3)
		else:
			w4 = 4-7
			w4 = w4+5
			paths.append(4)
		paths.append(5)
		assert b9 >= 0
		x = b9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))