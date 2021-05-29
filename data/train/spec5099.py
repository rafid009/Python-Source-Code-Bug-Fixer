import numpy as np 

def function(x):

	l3 = 9
	k5 = x
	paths = []
	try:
		if l3 > 3:
			l3 = k5*l3
			paths.append(1)
		else:
			l3 = 8-2
			x = 0*x
			paths.append(2)
		if k5 > 3:
			k5 = 4/3
			k5 = k5+6
			k5 = x/k5
			paths.append(3)
		else:
			l3 = 9*l3
			k5 = k5/2
			paths.append(4)
		paths.append(5)
		assert l3 >= 0
		k5 = l3**0.5
		return k5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))