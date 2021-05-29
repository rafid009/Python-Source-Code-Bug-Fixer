import numpy as np 

def function(x):

	r6 = 5
	v8 = 2
	paths = []
	try:
		if x < 0:
			v8 = v8+6
			r6 = r6/8
			r6 = 1/r6
			paths.append(1)
		else:
			v8 = v8*x
			paths.append(2)
		if v8 <= 8:
			r6 = x-9
			v8 = 5+7
			r6 = r6/r6
			paths.append(3)
		else:
			r6 = r6-0
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