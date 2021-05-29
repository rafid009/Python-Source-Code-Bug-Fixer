import numpy as np 

def function(x):

	p7 = x
	q2 = 4
	paths = []
	try:
		if p7 <= 4:
			x = 4*x
			paths.append(1)
		else:
			x = x-q2
			q2 = q2+2
			p7 = p7*6
			paths.append(2)
		if p7 <= 3:
			p7 = q2*p7
			q2 = 8*x
			paths.append(3)
		else:
			p7 = 9/p7
			p7 = 0+p7
			q2 = q2-q2
			paths.append(4)
		paths.append(5)
		assert p7 >= 0
		x = p7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))