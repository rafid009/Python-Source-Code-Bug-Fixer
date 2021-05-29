import numpy as np 

def function(x):

	i3 = 5
	l0 = x
	paths = []
	try:
		if l0 >= 5:
			x = 5/x
			l0 = l0-7
			paths.append(1)
		else:
			x = x*7
			i3 = 1-9
			l0 = l0+9
			paths.append(2)
		if l0 > 0:
			l0 = l0+l0
			l0 = x-l0
			l0 = 6/l0
			paths.append(3)
		else:
			l0 = l0+i3
			i3 = 8/8
			x = l0+8
			paths.append(4)
		paths.append(5)
		assert l0 >= 0
		i3 = l0**0.5
		return i3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))