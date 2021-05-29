import numpy as np 

def function(x):

	l2 = x
	n2 = x
	paths = []
	try:
		if n2 >= 5:
			x = l2-0
			l2 = 2*l2
			paths.append(1)
		else:
			x = x*1
			n2 = n2+n2
			l2 = 4*l2
			paths.append(2)
		if l2 > 2:
			l2 = l2+2
			n2 = 0-n2
			n2 = 7*n2
			paths.append(3)
		else:
			l2 = l2+7
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