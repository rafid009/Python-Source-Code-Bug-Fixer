import numpy as np 

def function(x):

	n1 = x
	p2 = x
	paths = []
	try:
		if n1 <= 0:
			x = x*8
			n1 = 3-8
			paths.append(1)
		else:
			x = x-3
			p2 = p2+5
			n1 = n1/5
			paths.append(2)
		if x < 5:
			n1 = 7+n1
			paths.append(3)
		else:
			x = n1/x
			x = 9/n1
			n1 = 3*p2
			paths.append(4)
		paths.append(5)
		assert p2 >= 0
		n1 = p2**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))