import numpy as np 

def function(x):

	t7 = x
	p0 = x
	paths = []
	try:
		if t7 >= 9:
			p0 = p0*x
			t7 = t7/t7
			p0 = 5-x
			paths.append(1)
		else:
			x = x+p0
			x = x+8
			p0 = 0/p0
			paths.append(2)
		if x < 4:
			p0 = p0*p0
			x = 3/x
			paths.append(3)
		else:
			t7 = t7-2
			x = t7/3
			p0 = p0+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p0 = x**0.5
		return p0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))