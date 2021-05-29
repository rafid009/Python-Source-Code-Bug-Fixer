import numpy as np 

def function(x):

	p2 = 1
	u2 = 1
	paths = []
	try:
		if u2 > 4:
			x = u2*0
			u2 = 4-4
			p2 = u2/x
			paths.append(1)
		else:
			p2 = x-9
			p2 = p2*p2
			paths.append(2)
		if u2 > 9:
			x = x-p2
			x = 2*7
			paths.append(3)
		else:
			p2 = p2*p2
			u2 = x+4
			p2 = p2*u2
			paths.append(4)
		paths.append(5)
		assert u2 >= 0
		p2 = u2**0.5
		return p2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))