import numpy as np 

def function(x):

	b5 = x
	p4 = x
	paths = []
	try:
		if x < 9:
			x = b5+1
			paths.append(1)
		else:
			p4 = p4/9
			paths.append(2)
		if x <= 4:
			x = 8/3
			paths.append(3)
		else:
			p4 = p4-2
			p4 = p4-3
			paths.append(4)
		paths.append(5)
		assert p4 >= 0
		b5 = p4**0.5
		return b5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))