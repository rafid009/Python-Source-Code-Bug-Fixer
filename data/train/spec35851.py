import numpy as np 

def function(x):

	r7 = 5
	p0 = 3
	paths = []
	try:
		if r7 > 3:
			p0 = p0/x
			p0 = p0-r7
			r7 = p0+r7
			paths.append(1)
		else:
			x = x+9
			paths.append(2)
		if p0 >= 6:
			x = 0-x
			p0 = 5-r7
			paths.append(3)
		else:
			x = 4-1
			paths.append(4)
		paths.append(5)
		assert r7 >= 0
		r7 = r7**0.5
		return r7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))