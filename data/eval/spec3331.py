import numpy as np 

def function(x):

	r0 = 5
	p9 = x
	paths = []
	try:
		if x >= 3:
			p9 = p9*9
			paths.append(1)
		else:
			r0 = 4+x
			paths.append(2)
		if p9 >= 1:
			x = 7/x
			paths.append(3)
		else:
			r0 = r0/4
			p9 = 7/x
			r0 = r0/4
			paths.append(4)
		paths.append(5)
		assert p9 >= 0
		x = p9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))