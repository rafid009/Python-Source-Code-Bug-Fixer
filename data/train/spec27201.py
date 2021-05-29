import numpy as np 

def function(x):

	l3 = 6
	l2 = x
	paths = []
	try:
		if l3 > 9:
			x = x*x
			l2 = l2*l2
			paths.append(1)
		else:
			l3 = 5*6
			x = 7+7
			paths.append(2)
		if l2 >= 6:
			l2 = l2+4
			l2 = l2*2
			l2 = l2/8
			paths.append(3)
		else:
			l3 = l3*l2
			x = l2-2
			paths.append(4)
		paths.append(5)
		assert l3 >= 0
		l2 = l3**0.5
		return l2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))