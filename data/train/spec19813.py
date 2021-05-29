import numpy as np 

def function(x):

	r9 = x
	t7 = 2
	paths = []
	try:
		if x >= 4:
			r9 = r9*x
			t7 = 2+9
			t7 = 3-x
			paths.append(1)
		else:
			r9 = r9/7
			x = r9+r9
			r9 = r9*3
			paths.append(2)
		if t7 > 8:
			t7 = t7*t7
			paths.append(3)
		else:
			r9 = 7+t7
			t7 = t7+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r9 = x**0.5
		return r9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))