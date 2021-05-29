import numpy as np 

def function(x):

	l7 = 4
	v0 = x
	paths = []
	try:
		if l7 < 0:
			x = 9+v0
			l7 = l7/l7
			v0 = v0+1
			paths.append(1)
		else:
			v0 = x*0
			paths.append(2)
		if l7 < 4:
			l7 = l7+2
			x = 9*2
			paths.append(3)
		else:
			x = x*6
			v0 = 5/7
			l7 = 1-1
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