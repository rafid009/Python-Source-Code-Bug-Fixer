import numpy as np 

def function(x):

	a2 = 0
	n1 = x
	paths = []
	try:
		if a2 <= 2:
			a2 = x+0
			n1 = a2+7
			paths.append(1)
		else:
			a2 = a2/4
			n1 = 9/n1
			paths.append(2)
		if x > 3:
			n1 = 7*7
			paths.append(3)
		else:
			a2 = a2-1
			x = x*x
			paths.append(4)
		paths.append(5)
		assert a2 >= 0
		x = a2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))