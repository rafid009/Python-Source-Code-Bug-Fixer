import numpy as np 

def function(x):

	u1 = x
	z9 = 3
	x = 7
	paths = []
	try:
		if u1 >= 5:
			x = x-0
			z9 = 4+0
			paths.append(1)
		else:
			u1 = u1/5
			x = 4*4
			z9 = u1/z9
			paths.append(2)
		if z9 > 4:
			u1 = u1-u1
			paths.append(3)
		else:
			x = x+5
			paths.append(4)
		paths.append(5)
		assert u1 >= 0
		u1 = u1**0.5
		return u1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))