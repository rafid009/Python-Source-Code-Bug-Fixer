import numpy as np 

def function(x):

	l6 = x
	i3 = x
	paths = []
	try:
		if x < 3:
			i3 = 7+9
			i3 = 9*l6
			x = 6+x
			paths.append(1)
		else:
			i3 = i3+7
			l6 = l6-7
			l6 = 8/l6
			paths.append(2)
		if i3 > 8:
			x = x/2
			x = x*x
			i3 = 2+4
			paths.append(3)
		else:
			i3 = i3*6
			x = 6/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))