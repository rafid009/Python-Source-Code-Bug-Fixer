import numpy as np 

def function(x):

	v4 = 1
	l5 = x
	paths = []
	try:
		if l5 <= 7:
			v4 = l5/5
			paths.append(1)
		else:
			v4 = v4-x
			l5 = l5*l5
			paths.append(2)
		if v4 < 1:
			l5 = 9-l5
			v4 = v4/5
			paths.append(3)
		else:
			x = 8-0
			paths.append(4)
		paths.append(5)
		assert v4 >= 0
		x = v4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))