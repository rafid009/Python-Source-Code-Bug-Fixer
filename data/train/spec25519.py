import numpy as np 

def function(x):

	l0 = x
	i3 = 0
	paths = []
	try:
		if x < 8:
			x = 2-6
			paths.append(1)
		else:
			x = x/4
			paths.append(2)
		if i3 <= 1:
			l0 = l0+4
			i3 = i3/8
			paths.append(3)
		else:
			x = 9/4
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