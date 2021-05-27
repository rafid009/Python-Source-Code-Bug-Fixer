import numpy as np 

def function(x):

	v8 = 2
	q5 = 3
	x = 9
	paths = []
	try:
		if x > 8:
			v8 = q5-x
			paths.append(1)
		else:
			x = 4-x
			x = x-x
			paths.append(2)
		if v8 > 4:
			v8 = 7+v8
			x = 4-q5
			paths.append(3)
		else:
			x = x/v8
			q5 = 3-0
			q5 = x-q5
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