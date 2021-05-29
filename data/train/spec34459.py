import numpy as np 

def function(x):

	l6 = x
	v2 = 7
	paths = []
	try:
		if l6 < 1:
			v2 = v2-v2
			paths.append(1)
		else:
			l6 = v2/7
			x = 5*x
			l6 = l6+1
			paths.append(2)
		if x >= 3:
			x = x+1
			l6 = x+l6
			v2 = 0+8
			paths.append(3)
		else:
			l6 = 0/l6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v2 = x**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))