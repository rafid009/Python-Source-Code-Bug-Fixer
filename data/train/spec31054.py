import numpy as np 

def function(x):

	p6 = x
	t0 = x
	paths = []
	try:
		if x >= 8:
			x = 6-x
			t0 = x/4
			paths.append(1)
		else:
			p6 = 3*p6
			p6 = 3-4
			p6 = p6/5
			paths.append(2)
		if x < 0:
			t0 = t0/8
			t0 = t0*2
			paths.append(3)
		else:
			t0 = t0/4
			x = t0+1
			paths.append(4)
		paths.append(5)
		assert t0 >= 0
		p6 = t0**0.5
		return p6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))