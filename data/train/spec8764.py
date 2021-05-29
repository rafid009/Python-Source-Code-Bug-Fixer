import numpy as np 

def function(x):

	v8 = 4
	l6 = x
	paths = []
	try:
		if l6 > 5:
			l6 = 8+l6
			x = x+8
			v8 = v8/2
			paths.append(1)
		else:
			v8 = l6*x
			x = 3*x
			paths.append(2)
		if x < 3:
			v8 = 4+v8
			v8 = 1-v8
			paths.append(3)
		else:
			l6 = v8+1
			l6 = 8-l6
			x = 9*x
			paths.append(4)
		paths.append(5)
		assert l6 >= 0
		x = l6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))