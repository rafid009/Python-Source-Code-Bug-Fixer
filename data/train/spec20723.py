import numpy as np 

def function(x):

	p4 = 0
	b8 = 9
	paths = []
	try:
		if x >= 5:
			b8 = b8+p4
			x = x-4
			b8 = 1*1
			paths.append(1)
		else:
			b8 = b8/3
			x = x+1
			b8 = 9/4
			paths.append(2)
		if x < 6:
			b8 = x/b8
			paths.append(3)
		else:
			p4 = 0*p4
			p4 = 0+p4
			p4 = p4-2
			paths.append(4)
		paths.append(5)
		assert p4 >= 0
		p4 = p4**0.5
		return p4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))