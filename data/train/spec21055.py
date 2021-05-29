import numpy as np 

def function(x):

	r6 = x
	z3 = x
	paths = []
	try:
		if r6 <= 7:
			x = r6+2
			paths.append(1)
		else:
			r6 = r6*x
			paths.append(2)
		if r6 >= 5:
			r6 = r6*z3
			r6 = r6-4
			paths.append(3)
		else:
			z3 = r6*8
			paths.append(4)
		paths.append(5)
		assert z3 >= 0
		r6 = z3**0.5
		return r6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))