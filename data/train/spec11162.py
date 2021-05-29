import numpy as np 

def function(x):

	v0 = 5
	l8 = x
	x = x
	paths = []
	try:
		if x < 8:
			x = x*0
			x = x-1
			x = x-9
			paths.append(1)
		else:
			v0 = 7/x
			v0 = v0/9
			l8 = l8-6
			paths.append(2)
		if v0 > 6:
			v0 = v0*1
			x = 0/x
			paths.append(3)
		else:
			l8 = x+l8
			l8 = 5+l8
			paths.append(4)
		paths.append(5)
		assert l8 >= 0
		l8 = l8**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))