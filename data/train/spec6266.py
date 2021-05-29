import numpy as np 

def function(x):

	v8 = x
	l3 = x
	paths = []
	try:
		if x < 7:
			l3 = l3/9
			x = v8/x
			paths.append(1)
		else:
			l3 = v8-4
			x = v8/v8
			paths.append(2)
		if x > 1:
			l3 = l3*6
			paths.append(3)
		else:
			l3 = v8/l3
			paths.append(4)
		paths.append(5)
		assert v8 >= 0
		x = v8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))