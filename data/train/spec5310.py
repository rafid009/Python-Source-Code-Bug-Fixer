import numpy as np 

def function(x):

	t1 = x
	r4 = x
	paths = []
	try:
		if t1 > 4:
			x = x+6
			paths.append(1)
		else:
			r4 = r4/x
			r4 = x-r4
			paths.append(2)
		if x > 6:
			t1 = 8-t1
			t1 = 6+t1
			t1 = 9/r4
			paths.append(3)
		else:
			r4 = r4*7
			paths.append(4)
		paths.append(5)
		assert t1 >= 0
		r4 = t1**0.5
		return r4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))