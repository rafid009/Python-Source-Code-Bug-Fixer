import numpy as np 

def function(x):

	l2 = x
	l3 = 5
	paths = []
	try:
		if l3 <= 6:
			l2 = l2/4
			x = 1+l2
			paths.append(1)
		else:
			l2 = 4+3
			paths.append(2)
		if l2 <= 8:
			l3 = l3+9
			l3 = x*2
			l3 = 5+l3
			paths.append(3)
		else:
			x = x*l2
			l2 = 3+1
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