import numpy as np 

def function(x):

	v5 = x
	l3 = x
	paths = []
	try:
		if x > 0:
			x = 0+0
			paths.append(1)
		else:
			v5 = 5*v5
			paths.append(2)
		if x < 4:
			v5 = 7-v5
			paths.append(3)
		else:
			l3 = 3*l3
			l3 = 9-l3
			l3 = 8/l3
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