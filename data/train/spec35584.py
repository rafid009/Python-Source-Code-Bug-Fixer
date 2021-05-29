import numpy as np 

def function(x):

	p9 = 4
	n4 = 3
	paths = []
	try:
		if x > 7:
			p9 = 2*p9
			p9 = 6/p9
			n4 = 7-n4
			paths.append(1)
		else:
			n4 = n4/5
			p9 = p9+5
			paths.append(2)
		if p9 >= 6:
			x = x+4
			n4 = x+6
			paths.append(3)
		else:
			n4 = n4/p9
			n4 = 5/n4
			paths.append(4)
		paths.append(5)
		assert n4 >= 0
		n4 = n4**0.5
		return n4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))