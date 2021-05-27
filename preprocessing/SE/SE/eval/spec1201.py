import numpy as np 

def function(x):

	l9 = x
	v7 = x
	paths = []
	try:
		if x > 5:
			x = x-x
			paths.append(1)
		else:
			v7 = 3+v7
			paths.append(2)
		if x < 0:
			x = x+v7
			paths.append(3)
		else:
			x = x+9
			paths.append(4)
		paths.append(5)
		assert l9 >= 0
		v7 = l9**0.5
		return v7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))