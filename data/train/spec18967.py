import numpy as np 

def function(x):

	v0 = x
	l7 = x
	paths = []
	try:
		if v0 > 6:
			x = v0/9
			paths.append(1)
		else:
			l7 = x/x
			paths.append(2)
		if l7 > 4:
			l7 = 2+1
			l7 = v0-l7
			paths.append(3)
		else:
			l7 = 3/x
			v0 = 8-l7
			x = x+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v0 = x**0.5
		return v0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))