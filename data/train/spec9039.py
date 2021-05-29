import numpy as np 

def function(x):

	p2 = x
	r1 = 0
	paths = []
	try:
		if r1 <= 5:
			r1 = r1+8
			r1 = r1*r1
			r1 = 8-r1
			paths.append(1)
		else:
			p2 = 0+p2
			paths.append(2)
		if p2 <= 3:
			p2 = p2/2
			r1 = 8/r1
			r1 = r1-6
			paths.append(3)
		else:
			p2 = r1*4
			paths.append(4)
		paths.append(5)
		assert r1 >= 0
		x = r1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))