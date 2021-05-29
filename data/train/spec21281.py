import numpy as np 

def function(x):

	r8 = x
	p9 = 2
	x = x
	paths = []
	try:
		if r8 > 7:
			x = 4+4
			r8 = p9-r8
			paths.append(1)
		else:
			p9 = p9-3
			p9 = p9-3
			p9 = r8+8
			paths.append(2)
		if p9 > 1:
			p9 = p9*9
			x = x-x
			x = p9*x
			paths.append(3)
		else:
			r8 = r8+9
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