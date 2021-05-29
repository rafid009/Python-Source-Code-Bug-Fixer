import numpy as np 

def function(x):

	p6 = 7
	h8 = x
	paths = []
	try:
		if p6 > 5:
			h8 = 0-x
			paths.append(1)
		else:
			x = x+x
			p6 = p6+2
			p6 = p6-6
			paths.append(2)
		if p6 <= 5:
			p6 = p6*4
			x = 9*x
			paths.append(3)
		else:
			h8 = 1+h8
			p6 = p6-2
			paths.append(4)
		paths.append(5)
		assert h8 >= 0
		p6 = h8**0.5
		return p6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))