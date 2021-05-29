import numpy as np 

def function(x):

	l5 = 8
	o3 = x
	paths = []
	try:
		if o3 > 0:
			l5 = l5-9
			paths.append(1)
		else:
			o3 = l5/1
			paths.append(2)
		if x >= 7:
			x = o3*l5
			l5 = l5-5
			x = x/x
			paths.append(3)
		else:
			l5 = 7*l5
			l5 = 0/l5
			paths.append(4)
		paths.append(5)
		assert l5 >= 0
		l5 = l5**0.5
		return l5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))