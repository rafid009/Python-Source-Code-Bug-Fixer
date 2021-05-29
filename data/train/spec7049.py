import numpy as np 

def function(x):

	l4 = 9
	v4 = 6
	paths = []
	try:
		if x <= 4:
			v4 = l4/x
			paths.append(1)
		else:
			x = v4/6
			l4 = 7*4
			x = x*5
			paths.append(2)
		if v4 <= 0:
			v4 = v4/4
			l4 = 9*2
			paths.append(3)
		else:
			v4 = v4+1
			l4 = l4/l4
			x = x*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l4 = x**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))