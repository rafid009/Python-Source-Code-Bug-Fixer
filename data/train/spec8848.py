import numpy as np 

def function(x):

	l2 = x
	n3 = 9
	paths = []
	try:
		if n3 >= 6:
			l2 = l2+x
			n3 = n3+l2
			paths.append(1)
		else:
			l2 = l2*4
			paths.append(2)
		if l2 >= 7:
			n3 = n3-1
			paths.append(3)
		else:
			x = l2-0
			paths.append(4)
		paths.append(5)
		assert l2 >= 0
		l2 = l2**0.5
		return l2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))