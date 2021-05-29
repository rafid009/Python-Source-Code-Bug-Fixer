import numpy as np 

def function(x):

	l0 = x
	o3 = 8
	paths = []
	try:
		if l0 >= 8:
			l0 = x+7
			o3 = o3-l0
			paths.append(1)
		else:
			o3 = 9+o3
			l0 = 1*x
			paths.append(2)
		if o3 >= 9:
			x = x+x
			x = x/7
			o3 = 7*o3
			paths.append(3)
		else:
			l0 = 9*l0
			l0 = 3*l0
			paths.append(4)
		paths.append(5)
		assert o3 >= 0
		l0 = o3**0.5
		return l0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))