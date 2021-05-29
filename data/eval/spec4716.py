import numpy as np 

def function(x):

	t1 = 5
	w0 = x
	paths = []
	try:
		if x < 4:
			x = 0*x
			paths.append(1)
		else:
			t1 = x+t1
			paths.append(2)
		if t1 <= 1:
			x = x/2
			t1 = t1-w0
			x = 5*x
			paths.append(3)
		else:
			t1 = 3-t1
			t1 = t1*3
			paths.append(4)
		paths.append(5)
		assert w0 >= 0
		x = w0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))