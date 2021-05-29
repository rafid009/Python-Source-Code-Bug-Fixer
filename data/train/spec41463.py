import numpy as np 

def function(x):

	v6 = 4
	l2 = 4
	paths = []
	try:
		if l2 < 6:
			l2 = l2+0
			l2 = l2-2
			l2 = 9/l2
			paths.append(1)
		else:
			v6 = 5/v6
			l2 = l2+7
			paths.append(2)
		if x < 0:
			v6 = v6+x
			x = 8+1
			x = 3+v6
			paths.append(3)
		else:
			l2 = x-4
			l2 = 0-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l2 = x**0.5
		return l2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))