import numpy as np 

def function(x):

	v8 = 3
	r8 = x
	paths = []
	try:
		if v8 > 1:
			r8 = 8-r8
			r8 = 6*x
			r8 = 9+6
			paths.append(1)
		else:
			r8 = r8-4
			x = r8*x
			paths.append(2)
		if x > 3:
			v8 = 7+3
			r8 = r8/5
			r8 = r8+r8
			paths.append(3)
		else:
			r8 = 7+0
			v8 = v8/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v8 = x**0.5
		return v8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))