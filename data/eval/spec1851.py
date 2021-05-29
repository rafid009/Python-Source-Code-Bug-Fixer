import numpy as np 

def function(x):

	j6 = x
	w4 = 8
	paths = []
	try:
		if w4 <= 6:
			w4 = 5/w4
			paths.append(1)
		else:
			x = x-x
			w4 = w4*j6
			paths.append(2)
		if j6 > 8:
			w4 = 4/w4
			j6 = j6*8
			x = x+2
			paths.append(3)
		else:
			j6 = j6*1
			x = w4-2
			paths.append(4)
		paths.append(5)
		assert w4 >= 0
		x = w4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))