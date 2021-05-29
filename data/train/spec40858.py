import numpy as np 

def function(x):

	p4 = x
	h9 = 8
	paths = []
	try:
		if p4 >= 9:
			x = 0+x
			x = 2*9
			paths.append(1)
		else:
			x = 6/x
			paths.append(2)
		if h9 <= 3:
			x = x-6
			h9 = 2-2
			paths.append(3)
		else:
			x = x*2
			p4 = 2+p4
			h9 = 0+1
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