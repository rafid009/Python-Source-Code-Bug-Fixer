import numpy as np 

def function(x):

	a1 = 4
	l3 = 0
	paths = []
	try:
		if x >= 7:
			x = 7+x
			a1 = 7-a1
			a1 = l3-a1
			paths.append(1)
		else:
			a1 = a1-a1
			l3 = x-l3
			x = x*a1
			paths.append(2)
		if l3 >= 8:
			a1 = a1/l3
			paths.append(3)
		else:
			l3 = 2-l3
			paths.append(4)
		paths.append(5)
		assert l3 >= 0
		x = l3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))