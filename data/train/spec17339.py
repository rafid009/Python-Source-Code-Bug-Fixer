import numpy as np 

def function(x):

	t0 = 6
	p3 = x
	paths = []
	try:
		if p3 > 1:
			t0 = t0+3
			p3 = t0+p3
			t0 = p3/4
			paths.append(1)
		else:
			x = 1-8
			paths.append(2)
		if x < 1:
			t0 = t0/7
			paths.append(3)
		else:
			t0 = 0*t0
			p3 = x/5
			x = x/x
			paths.append(4)
		paths.append(5)
		assert p3 >= 0
		p3 = p3**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))