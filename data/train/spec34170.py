import numpy as np 

def function(x):

	b8 = x
	p3 = 2
	paths = []
	try:
		if b8 <= 3:
			p3 = 4*6
			paths.append(1)
		else:
			p3 = p3/4
			p3 = 6*1
			p3 = 2*p3
			paths.append(2)
		if b8 <= 9:
			x = 2+2
			paths.append(3)
		else:
			b8 = b8/3
			paths.append(4)
		paths.append(5)
		assert b8 >= 0
		b8 = b8**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))