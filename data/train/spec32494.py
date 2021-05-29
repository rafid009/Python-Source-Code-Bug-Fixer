import numpy as np 

def function(x):

	r0 = 6
	p2 = x
	paths = []
	try:
		if r0 < 7:
			r0 = 4+r0
			x = 9/p2
			paths.append(1)
		else:
			x = 3/2
			x = x/1
			x = p2-7
			paths.append(2)
		if x >= 8:
			p2 = p2/p2
			r0 = 0*9
			paths.append(3)
		else:
			r0 = x/2
			p2 = p2+x
			r0 = r0-3
			paths.append(4)
		paths.append(5)
		assert r0 >= 0
		x = r0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))