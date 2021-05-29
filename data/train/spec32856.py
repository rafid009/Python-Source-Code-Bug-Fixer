import numpy as np 

def function(x):

	l0 = x
	u2 = 6
	paths = []
	try:
		if l0 <= 1:
			x = x+4
			u2 = u2-l0
			paths.append(1)
		else:
			x = 0+x
			l0 = l0+l0
			l0 = 0+u2
			paths.append(2)
		if x > 5:
			u2 = 5*6
			l0 = 0*x
			u2 = 2/u2
			paths.append(3)
		else:
			l0 = l0+6
			x = x*2
			u2 = 5+9
			paths.append(4)
		paths.append(5)
		assert l0 >= 0
		l0 = l0**0.5
		return l0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))