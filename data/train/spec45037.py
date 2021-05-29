import numpy as np 

def function(x):

	a5 = x
	v8 = 1
	paths = []
	try:
		if a5 >= 3:
			v8 = v8*x
			a5 = a5/v8
			a5 = 2+x
			paths.append(1)
		else:
			v8 = v8+x
			paths.append(2)
		if v8 <= 5:
			v8 = 2-v8
			paths.append(3)
		else:
			v8 = v8+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a5 = x**0.5
		return a5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))