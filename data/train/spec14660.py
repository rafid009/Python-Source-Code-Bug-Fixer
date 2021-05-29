import numpy as np 

def function(x):

	t0 = x
	w6 = x
	paths = []
	try:
		if w6 >= 1:
			w6 = 4*w6
			t0 = 5/t0
			t0 = 2/t0
			paths.append(1)
		else:
			w6 = w6+4
			x = w6+2
			w6 = w6+9
			paths.append(2)
		if t0 >= 4:
			w6 = 3-t0
			x = x/w6
			paths.append(3)
		else:
			w6 = w6+t0
			w6 = 2/w6
			paths.append(4)
		paths.append(5)
		assert w6 >= 0
		x = w6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))