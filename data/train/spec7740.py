import numpy as np 

def function(x):

	n9 = x
	l0 = x
	paths = []
	try:
		if n9 < 5:
			n9 = 5-1
			x = 9+x
			n9 = n9+7
			paths.append(1)
		else:
			l0 = 7+1
			x = x/l0
			paths.append(2)
		if x > 5:
			x = 3-x
			paths.append(3)
		else:
			l0 = l0+0
			x = x-n9
			n9 = x-6
			paths.append(4)
		paths.append(5)
		assert l0 >= 0
		l0 = l0**0.5
		return l0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))