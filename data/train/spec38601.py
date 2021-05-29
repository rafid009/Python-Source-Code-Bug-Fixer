import numpy as np 

def function(x):

	t4 = 9
	p0 = x
	paths = []
	try:
		if t4 >= 6:
			x = 0+5
			t4 = t4/p0
			paths.append(1)
		else:
			p0 = p0*t4
			t4 = t4*x
			p0 = p0/t4
			paths.append(2)
		if x > 6:
			t4 = 8*8
			t4 = x*4
			p0 = p0+5
			paths.append(3)
		else:
			x = x*9
			x = 9-p0
			p0 = 7/p0
			paths.append(4)
		paths.append(5)
		assert p0 >= 0
		p0 = p0**0.5
		return p0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))