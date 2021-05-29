import numpy as np 

def function(x):

	u1 = x
	p8 = x
	paths = []
	try:
		if u1 < 1:
			u1 = u1/2
			paths.append(1)
		else:
			u1 = 1*u1
			x = x*7
			x = 4/x
			paths.append(2)
		if u1 >= 1:
			p8 = p8-2
			u1 = u1*2
			paths.append(3)
		else:
			x = x/5
			x = u1-u1
			p8 = 2-p8
			paths.append(4)
		paths.append(5)
		assert p8 >= 0
		x = p8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))