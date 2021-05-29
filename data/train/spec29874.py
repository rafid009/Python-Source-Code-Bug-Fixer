import numpy as np 

def function(x):

	p1 = 6
	r8 = x
	paths = []
	try:
		if r8 <= 0:
			p1 = p1*8
			p1 = 9+9
			paths.append(1)
		else:
			x = 5+x
			p1 = 7*x
			r8 = p1*r8
			paths.append(2)
		if r8 < 2:
			r8 = p1*5
			paths.append(3)
		else:
			x = 4-9
			r8 = 5/4
			r8 = r8-4
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