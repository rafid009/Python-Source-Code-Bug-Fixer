import numpy as np 

def function(x):

	f4 = x
	z3 = x
	paths = []
	try:
		if f4 >= 6:
			f4 = 7/f4
			paths.append(1)
		else:
			z3 = z3/5
			f4 = f4*0
			paths.append(2)
		if z3 < 0:
			z3 = z3/2
			z3 = 4/z3
			z3 = z3*1
			paths.append(3)
		else:
			f4 = x-8
			x = 8-x
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		f4 = f4**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))