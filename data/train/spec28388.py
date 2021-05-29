import numpy as np 

def function(x):

	o0 = 3
	a5 = x
	paths = []
	try:
		if x < 6:
			a5 = a5+o0
			a5 = a5-1
			paths.append(1)
		else:
			x = x+4
			paths.append(2)
		if a5 > 9:
			o0 = o0/8
			paths.append(3)
		else:
			o0 = 7+o0
			o0 = o0+a5
			a5 = a5+7
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		x = a5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))