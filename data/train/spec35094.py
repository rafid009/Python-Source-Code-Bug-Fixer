import numpy as np 

def function(x):

	r8 = x
	l2 = 6
	paths = []
	try:
		if r8 <= 1:
			l2 = 6+4
			r8 = r8*1
			r8 = 6*r8
			paths.append(1)
		else:
			l2 = 4*r8
			paths.append(2)
		if r8 < 7:
			x = 2-7
			paths.append(3)
		else:
			l2 = l2+l2
			l2 = 1*l2
			x = x*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l2 = x**0.5
		return l2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))