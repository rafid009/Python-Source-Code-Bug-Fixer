import numpy as np 

def function(x):

	t1 = x
	w0 = 1
	paths = []
	try:
		if t1 < 6:
			w0 = w0+4
			paths.append(1)
		else:
			t1 = t1+t1
			paths.append(2)
		if x <= 8:
			x = 4/x
			t1 = t1*2
			paths.append(3)
		else:
			x = 7+x
			t1 = 6/t1
			t1 = x*x
			paths.append(4)
		paths.append(5)
		assert t1 >= 0
		x = t1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))