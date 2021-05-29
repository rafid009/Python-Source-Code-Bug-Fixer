import numpy as np 

def function(x):

	n3 = 8
	p9 = x
	paths = []
	try:
		if n3 <= 2:
			p9 = p9/9
			paths.append(1)
		else:
			x = 9*x
			paths.append(2)
		if p9 <= 5:
			n3 = x*n3
			p9 = 4/p9
			paths.append(3)
		else:
			n3 = n3+3
			paths.append(4)
		paths.append(5)
		assert n3 >= 0
		n3 = n3**0.5
		return n3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))