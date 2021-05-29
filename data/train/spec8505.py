import numpy as np 

def function(x):

	j9 = x
	p4 = x
	paths = []
	try:
		if x <= 3:
			x = j9*2
			p4 = p4+p4
			x = x-x
			paths.append(1)
		else:
			x = 0*x
			paths.append(2)
		if p4 < 7:
			p4 = p4-0
			j9 = 6-4
			paths.append(3)
		else:
			p4 = j9+4
			paths.append(4)
		paths.append(5)
		assert p4 >= 0
		x = p4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))