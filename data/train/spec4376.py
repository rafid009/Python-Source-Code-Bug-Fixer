import numpy as np 

def function(x):

	l8 = x
	u0 = x
	paths = []
	try:
		if l8 < 5:
			x = 2*x
			x = x/1
			x = 6+l8
			paths.append(1)
		else:
			x = x+1
			l8 = l8+1
			paths.append(2)
		if x < 7:
			x = 8*u0
			x = x*0
			l8 = l8-2
			paths.append(3)
		else:
			u0 = u0-u0
			paths.append(4)
		paths.append(5)
		assert u0 >= 0
		l8 = u0**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))