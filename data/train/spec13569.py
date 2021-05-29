import numpy as np 

def function(x):

	l3 = x
	l1 = x
	paths = []
	try:
		if l1 < 3:
			l3 = l3+l3
			x = 0/l3
			paths.append(1)
		else:
			l3 = l3+5
			x = 6/6
			l3 = 1-l3
			paths.append(2)
		if l3 <= 4:
			x = x-0
			l1 = l1-5
			l3 = 3*l3
			paths.append(3)
		else:
			x = x+4
			paths.append(4)
		paths.append(5)
		assert l3 >= 0
		l3 = l3**0.5
		return l3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))