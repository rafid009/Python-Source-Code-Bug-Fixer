import numpy as np 

def function(x):

	l2 = 3
	r3 = 8
	paths = []
	try:
		if r3 >= 7:
			l2 = l2-x
			x = x-2
			paths.append(1)
		else:
			x = r3/x
			l2 = l2-9
			r3 = r3*1
			paths.append(2)
		if l2 >= 3:
			l2 = 9+l2
			paths.append(3)
		else:
			r3 = x/8
			l2 = 9/l2
			paths.append(4)
		paths.append(5)
		assert l2 >= 0
		r3 = l2**0.5
		return r3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))