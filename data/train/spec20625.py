import numpy as np 

def function(x):

	j2 = x
	v8 = 6
	paths = []
	try:
		if j2 <= 3:
			x = 7-8
			paths.append(1)
		else:
			v8 = v8-8
			v8 = 3-x
			x = x+5
			paths.append(2)
		if j2 <= 9:
			v8 = 6+8
			paths.append(3)
		else:
			x = 7*x
			v8 = 3-v8
			j2 = j2/x
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