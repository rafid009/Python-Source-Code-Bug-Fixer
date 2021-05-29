import numpy as np 

def function(x):

	r1 = x
	v8 = 3
	paths = []
	try:
		if x > 1:
			v8 = v8*9
			r1 = v8-7
			paths.append(1)
		else:
			v8 = v8+x
			paths.append(2)
		if r1 >= 9:
			r1 = 8+r1
			paths.append(3)
		else:
			r1 = r1*3
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