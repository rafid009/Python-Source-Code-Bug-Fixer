import numpy as np 

def function(x):

	f7 = 6
	p4 = x
	paths = []
	try:
		if p4 < 1:
			p4 = p4-6
			f7 = 3+f7
			paths.append(1)
		else:
			x = x/x
			p4 = p4/p4
			paths.append(2)
		if p4 >= 4:
			f7 = p4+4
			paths.append(3)
		else:
			p4 = x+1
			f7 = f7/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))