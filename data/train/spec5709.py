import numpy as np 

def function(x):

	l9 = 0
	v0 = 0
	paths = []
	try:
		if x > 1:
			l9 = l9-7
			paths.append(1)
		else:
			v0 = 5/2
			l9 = l9*7
			paths.append(2)
		if v0 <= 6:
			x = 3+l9
			x = x-2
			v0 = 9+0
			paths.append(3)
		else:
			x = x*6
			x = v0/l9
			paths.append(4)
		paths.append(5)
		assert l9 >= 0
		v0 = l9**0.5
		return v0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))