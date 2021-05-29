import numpy as np 

def function(x):

	p0 = x
	t6 = x
	paths = []
	try:
		if p0 > 5:
			t6 = t6-8
			x = 5-x
			paths.append(1)
		else:
			t6 = t6-4
			p0 = p0-6
			t6 = t6*x
			paths.append(2)
		if p0 < 1:
			t6 = p0/6
			x = x-0
			t6 = p0+1
			paths.append(3)
		else:
			p0 = p0/p0
			p0 = 0-9
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