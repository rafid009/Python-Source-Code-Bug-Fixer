import numpy as np 

def function(x):

	u9 = x
	l2 = 4
	x = x
	paths = []
	try:
		if u9 < 0:
			l2 = 9+l2
			x = x+u9
			x = x/7
			paths.append(1)
		else:
			x = 9+x
			l2 = l2*4
			paths.append(2)
		if x < 8:
			x = x*9
			paths.append(3)
		else:
			x = u9+x
			l2 = l2+0
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