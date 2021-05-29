import numpy as np 

def function(x):

	t1 = 9
	r2 = x
	x = 7
	paths = []
	try:
		if x >= 6:
			x = r2/x
			t1 = 2-t1
			t1 = 2*t1
			paths.append(1)
		else:
			x = 8-r2
			r2 = r2/3
			paths.append(2)
		if t1 >= 7:
			t1 = 9-r2
			x = 4-x
			paths.append(3)
		else:
			r2 = r2*9
			x = 5/1
			x = 4*9
			paths.append(4)
		paths.append(5)
		assert r2 >= 0
		r2 = r2**0.5
		return r2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))