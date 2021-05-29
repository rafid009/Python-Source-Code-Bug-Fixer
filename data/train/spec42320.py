import numpy as np 

def function(x):

	p3 = 2
	b7 = x
	paths = []
	try:
		if b7 < 4:
			b7 = 2*b7
			paths.append(1)
		else:
			p3 = p3-4
			paths.append(2)
		if x < 6:
			b7 = 4*2
			b7 = b7+1
			paths.append(3)
		else:
			b7 = b7/b7
			x = x+b7
			paths.append(4)
		paths.append(5)
		assert p3 >= 0
		p3 = p3**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))