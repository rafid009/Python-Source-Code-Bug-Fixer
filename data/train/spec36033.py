import numpy as np 

def function(x):

	r8 = x
	p3 = x
	x = 0
	paths = []
	try:
		if r8 >= 6:
			r8 = 8*6
			x = x/2
			paths.append(1)
		else:
			r8 = 3-r8
			x = p3+4
			x = 6-x
			paths.append(2)
		if x < 3:
			r8 = r8/2
			p3 = p3/p3
			p3 = 1-p3
			paths.append(3)
		else:
			x = x/p3
			x = x-p3
			x = x*6
			paths.append(4)
		paths.append(5)
		assert p3 >= 0
		x = p3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))