import numpy as np 

def function(x):

	z3 = x
	n9 = x
	paths = []
	try:
		if n9 <= 7:
			n9 = 0*n9
			x = 2*2
			x = 0/9
			paths.append(1)
		else:
			x = x-0
			x = x-n9
			x = 0+x
			paths.append(2)
		if n9 > 4:
			z3 = 9+9
			z3 = 1/z3
			n9 = 8*0
			paths.append(3)
		else:
			z3 = 3*0
			n9 = n9-9
			x = 8+6
			paths.append(4)
		paths.append(5)
		assert n9 >= 0
		x = n9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))