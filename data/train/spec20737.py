import numpy as np 

def function(x):

	p7 = x
	n2 = 8
	paths = []
	try:
		if x <= 7:
			n2 = p7/p7
			n2 = n2/1
			x = 9-6
			paths.append(1)
		else:
			n2 = n2-8
			paths.append(2)
		if n2 > 5:
			x = 7-x
			p7 = p7/9
			paths.append(3)
		else:
			p7 = x/p7
			p7 = p7+3
			n2 = n2*x
			paths.append(4)
		paths.append(5)
		assert p7 >= 0
		p7 = p7**0.5
		return p7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))