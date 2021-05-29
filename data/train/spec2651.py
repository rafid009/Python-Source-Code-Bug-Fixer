import numpy as np 

def function(x):

	p2 = x
	b3 = 5
	paths = []
	try:
		if x <= 9:
			p2 = p2*8
			paths.append(1)
		else:
			b3 = 1/6
			x = 6-8
			paths.append(2)
		if p2 > 3:
			b3 = 3/1
			b3 = 1+x
			paths.append(3)
		else:
			p2 = p2/x
			b3 = 6/b3
			paths.append(4)
		paths.append(5)
		assert b3 >= 0
		p2 = b3**0.5
		return p2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))