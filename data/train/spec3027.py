import numpy as np 

def function(x):

	z4 = 0
	b6 = 9
	paths = []
	try:
		if x >= 7:
			b6 = b6*2
			b6 = b6*x
			x = 9*8
			paths.append(1)
		else:
			b6 = b6+8
			b6 = 1/b6
			paths.append(2)
		if b6 >= 3:
			z4 = z4*1
			x = x+2
			b6 = 9-0
			paths.append(3)
		else:
			b6 = x*7
			b6 = b6-2
			b6 = b6-6
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		b6 = b6**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))