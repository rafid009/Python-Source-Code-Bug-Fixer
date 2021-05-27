import numpy as np 

def function(x):

	l0 = x
	n2 = x
	paths = []
	try:
		if l0 > 8:
			n2 = n2+x
			n2 = n2+n2
			paths.append(1)
		else:
			l0 = 0*5
			x = 5/x
			paths.append(2)
		if x <= 7:
			x = x*x
			n2 = n2*n2
			l0 = x*8
			paths.append(3)
		else:
			n2 = 8/n2
			l0 = 2-l0
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