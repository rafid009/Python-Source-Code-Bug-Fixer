import numpy as np 

def function(x):

	p6 = 0
	r8 = 7
	paths = []
	try:
		if p6 <= 7:
			r8 = x+r8
			x = r8-3
			paths.append(1)
		else:
			r8 = p6+r8
			r8 = 2*r8
			r8 = r8*r8
			paths.append(2)
		if x < 9:
			r8 = r8-1
			x = x+2
			paths.append(3)
		else:
			p6 = p6+4
			p6 = 4*p6
			paths.append(4)
		paths.append(5)
		assert r8 >= 0
		x = r8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))