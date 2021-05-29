import numpy as np 

def function(x):

	r7 = 9
	t1 = 6
	paths = []
	try:
		if r7 >= 1:
			t1 = t1-8
			x = 6+6
			paths.append(1)
		else:
			r7 = r7/r7
			r7 = r7/x
			x = x*t1
			paths.append(2)
		if t1 <= 4:
			x = 6-r7
			t1 = t1*x
			paths.append(3)
		else:
			t1 = 7/1
			r7 = r7-r7
			t1 = t1*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))