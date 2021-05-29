import numpy as np 

def function(x):

	n9 = 9
	a9 = x
	paths = []
	try:
		if x > 7:
			n9 = n9/x
			paths.append(1)
		else:
			x = x/9
			a9 = a9*0
			paths.append(2)
		if n9 > 9:
			n9 = n9/5
			paths.append(3)
		else:
			x = x+x
			n9 = x-n9
			n9 = 7/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n9 = x**0.5
		return n9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))