import numpy as np 

def function(x):

	n9 = x
	a1 = x
	paths = []
	try:
		if a1 > 1:
			a1 = 2+8
			n9 = 7*n9
			paths.append(1)
		else:
			n9 = 3+2
			x = 9*5
			a1 = a1+7
			paths.append(2)
		if n9 > 7:
			x = x/1
			x = x/7
			paths.append(3)
		else:
			x = x+a1
			paths.append(4)
		paths.append(5)
		assert a1 >= 0
		x = a1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))