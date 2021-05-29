import numpy as np 

def function(x):

	r7 = 4
	t2 = x
	paths = []
	try:
		if x < 0:
			t2 = t2/2
			r7 = r7-r7
			t2 = r7-t2
			paths.append(1)
		else:
			r7 = 5/r7
			r7 = 2*7
			paths.append(2)
		if r7 <= 2:
			t2 = t2/9
			r7 = r7-5
			paths.append(3)
		else:
			r7 = 9/r7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r7 = x**0.5
		return r7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))