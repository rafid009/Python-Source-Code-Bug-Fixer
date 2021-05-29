import numpy as np 

def function(x):

	n2 = x
	r5 = x
	paths = []
	try:
		if n2 < 8:
			x = n2*r5
			r5 = 0-r5
			paths.append(1)
		else:
			x = x/4
			n2 = 7*r5
			n2 = 3/n2
			paths.append(2)
		if r5 >= 6:
			r5 = 3+n2
			x = 9-x
			paths.append(3)
		else:
			n2 = n2-r5
			n2 = n2*7
			x = 7/8
			paths.append(4)
		paths.append(5)
		assert r5 >= 0
		x = r5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))