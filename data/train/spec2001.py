import numpy as np 

def function(x):

	l9 = 8
	v1 = x
	paths = []
	try:
		if x <= 5:
			l9 = 8+8
			paths.append(1)
		else:
			v1 = 1/6
			paths.append(2)
		if l9 >= 1:
			x = x/4
			v1 = v1*7
			paths.append(3)
		else:
			v1 = v1+4
			paths.append(4)
		paths.append(5)
		assert v1 >= 0
		x = v1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))