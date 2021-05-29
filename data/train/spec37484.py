import numpy as np 

def function(x):

	p0 = 8
	t6 = 8
	x = 3
	paths = []
	try:
		if t6 < 7:
			t6 = 4/t6
			p0 = p0/p0
			paths.append(1)
		else:
			x = 8+x
			paths.append(2)
		if t6 < 3:
			x = p0*x
			x = p0+3
			paths.append(3)
		else:
			t6 = 1-t6
			x = x/8
			p0 = p0-4
			paths.append(4)
		paths.append(5)
		assert t6 >= 0
		p0 = t6**0.5
		return p0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))