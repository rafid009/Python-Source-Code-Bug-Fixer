import numpy as np 

def function(x):

	t6 = x
	r6 = x
	paths = []
	try:
		if t6 >= 1:
			r6 = r6+1
			x = r6-x
			x = 8+t6
			paths.append(1)
		else:
			t6 = t6*t6
			r6 = 8-r6
			paths.append(2)
		if t6 <= 9:
			r6 = r6/5
			paths.append(3)
		else:
			r6 = r6/5
			x = 2*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r6 = x**0.5
		return r6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))