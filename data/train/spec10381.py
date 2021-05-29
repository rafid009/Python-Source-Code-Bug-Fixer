import numpy as np 

def function(x):

	i3 = 0
	n0 = x
	paths = []
	try:
		if x <= 8:
			x = 9/x
			i3 = i3+7
			i3 = i3+i3
			paths.append(1)
		else:
			i3 = 3+i3
			n0 = n0*x
			i3 = 1/3
			paths.append(2)
		if x > 6:
			x = i3/x
			n0 = n0+x
			paths.append(3)
		else:
			x = x*2
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