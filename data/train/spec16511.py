import numpy as np 

def function(x):

	r8 = x
	l7 = 9
	paths = []
	try:
		if l7 < 1:
			r8 = r8*8
			x = x*r8
			r8 = 7+r8
			paths.append(1)
		else:
			l7 = 9/l7
			x = 2+x
			l7 = 5*r8
			paths.append(2)
		if x >= 4:
			r8 = r8-5
			x = 4*x
			paths.append(3)
		else:
			x = 9-x
			paths.append(4)
		paths.append(5)
		assert l7 >= 0
		l7 = l7**0.5
		return l7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))