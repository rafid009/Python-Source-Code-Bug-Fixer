import numpy as np 

def function(x):

	l1 = x
	a1 = 1
	paths = []
	try:
		if x <= 2:
			x = x*a1
			paths.append(1)
		else:
			x = x-a1
			x = 3/a1
			x = x+x
			paths.append(2)
		if l1 > 2:
			a1 = a1+a1
			a1 = a1+8
			paths.append(3)
		else:
			a1 = 2+1
			x = x-4
			paths.append(4)
		paths.append(5)
		assert l1 >= 0
		x = l1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))