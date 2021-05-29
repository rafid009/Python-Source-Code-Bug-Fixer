import numpy as np 

def function(x):

	n5 = 0
	w1 = 9
	paths = []
	try:
		if n5 < 4:
			n5 = x/8
			n5 = n5/7
			x = w1/x
			paths.append(1)
		else:
			x = x*8
			paths.append(2)
		if n5 <= 0:
			n5 = x-1
			w1 = 2-n5
			paths.append(3)
		else:
			n5 = n5+n5
			paths.append(4)
		paths.append(5)
		assert n5 >= 0
		x = n5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))