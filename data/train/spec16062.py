import numpy as np 

def function(x):

	l1 = x
	r8 = x
	paths = []
	try:
		if r8 > 6:
			x = 7-x
			paths.append(1)
		else:
			l1 = 5-l1
			r8 = r8+l1
			r8 = 4-r8
			paths.append(2)
		if r8 > 7:
			x = 4*r8
			paths.append(3)
		else:
			l1 = x/l1
			paths.append(4)
		paths.append(5)
		assert l1 >= 0
		r8 = l1**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))