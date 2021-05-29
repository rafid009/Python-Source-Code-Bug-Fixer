import numpy as np 

def function(x):

	b4 = x
	l3 = x
	paths = []
	try:
		if b4 > 1:
			b4 = x/b4
			l3 = 7/4
			x = 1-2
			paths.append(1)
		else:
			x = x+2
			l3 = 2-l3
			paths.append(2)
		if b4 < 2:
			l3 = 7/l3
			l3 = x+x
			paths.append(3)
		else:
			x = 9-5
			l3 = 4*l3
			l3 = l3+8
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