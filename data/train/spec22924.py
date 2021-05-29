import numpy as np 

def function(x):

	r7 = 2
	p0 = x
	paths = []
	try:
		if p0 < 5:
			p0 = p0/p0
			paths.append(1)
		else:
			r7 = r7-4
			paths.append(2)
		if x > 4:
			p0 = 6+p0
			paths.append(3)
		else:
			r7 = 8/x
			paths.append(4)
		paths.append(5)
		assert r7 >= 0
		p0 = r7**0.5
		return p0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))