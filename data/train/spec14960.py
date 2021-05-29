import numpy as np 

def function(x):

	t6 = x
	w8 = 4
	paths = []
	try:
		if x > 7:
			t6 = 7/x
			w8 = 8-w8
			paths.append(1)
		else:
			w8 = t6-x
			t6 = t6+t6
			paths.append(2)
		if t6 <= 6:
			w8 = w8-1
			x = 7+3
			x = x*x
			paths.append(3)
		else:
			w8 = 2-0
			paths.append(4)
		paths.append(5)
		assert t6 >= 0
		x = t6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))