import numpy as np 

def function(x):

	l3 = x
	l7 = x
	x = 6
	paths = []
	try:
		if l7 <= 9:
			x = x+5
			x = l7+x
			paths.append(1)
		else:
			l7 = l3*l3
			paths.append(2)
		if x > 1:
			l3 = l3-2
			paths.append(3)
		else:
			l7 = 0/3
			l3 = l3/4
			paths.append(4)
		paths.append(5)
		assert l7 >= 0
		l3 = l7**0.5
		return l3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))