import numpy as np 

def function(x):

	p4 = 8
	i4 = x
	paths = []
	try:
		if p4 >= 3:
			i4 = 5/x
			i4 = x/p4
			i4 = x/5
			paths.append(1)
		else:
			i4 = 7-i4
			paths.append(2)
		if x > 9:
			x = x+9
			x = 9*x
			paths.append(3)
		else:
			p4 = p4-9
			p4 = p4/p4
			x = x+8
			paths.append(4)
		paths.append(5)
		assert i4 >= 0
		p4 = i4**0.5
		return p4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))