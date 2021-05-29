import numpy as np 

def function(x):

	v6 = 4
	l1 = 8
	paths = []
	try:
		if x > 7:
			l1 = l1+l1
			x = x-3
			x = v6+x
			paths.append(1)
		else:
			l1 = 1*l1
			paths.append(2)
		if x > 7:
			x = 4+x
			paths.append(3)
		else:
			l1 = x/l1
			v6 = x-v6
			x = x+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l1 = x**0.5
		return l1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))