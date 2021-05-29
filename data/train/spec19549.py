import numpy as np 

def function(x):

	p4 = 7
	u3 = x
	paths = []
	try:
		if x < 8:
			p4 = 9/p4
			paths.append(1)
		else:
			x = x+8
			x = 5+x
			paths.append(2)
		if p4 < 5:
			x = 4-5
			u3 = p4+x
			paths.append(3)
		else:
			x = x*x
			p4 = p4-0
			x = u3*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u3 = x**0.5
		return u3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))