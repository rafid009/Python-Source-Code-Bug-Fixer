import numpy as np 

def function(x):

	z3 = x
	m1 = 3
	paths = []
	try:
		if x < 6:
			x = 4+x
			m1 = x-m1
			paths.append(1)
		else:
			z3 = 7-m1
			paths.append(2)
		if m1 <= 7:
			z3 = z3-z3
			paths.append(3)
		else:
			x = x*8
			x = x+0
			paths.append(4)
		paths.append(5)
		assert m1 >= 0
		x = m1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))