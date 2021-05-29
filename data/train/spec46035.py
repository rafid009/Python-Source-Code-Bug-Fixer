import numpy as np 

def function(x):

	p1 = 4
	v7 = 0
	paths = []
	try:
		if x < 0:
			p1 = v7*4
			paths.append(1)
		else:
			x = 6/8
			paths.append(2)
		if p1 < 7:
			p1 = p1+8
			p1 = x/2
			paths.append(3)
		else:
			p1 = p1-8
			v7 = 8-v7
			paths.append(4)
		paths.append(5)
		assert p1 >= 0
		v7 = p1**0.5
		return v7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))