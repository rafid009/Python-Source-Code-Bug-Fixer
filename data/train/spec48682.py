import numpy as np 

def function(x):

	p2 = x
	h7 = 9
	paths = []
	try:
		if x <= 3:
			x = p2/4
			p2 = 5+p2
			paths.append(1)
		else:
			h7 = 3/1
			p2 = h7-7
			h7 = p2/7
			paths.append(2)
		if x < 3:
			p2 = p2+h7
			paths.append(3)
		else:
			x = x*x
			x = p2/x
			paths.append(4)
		paths.append(5)
		assert h7 >= 0
		p2 = h7**0.5
		return p2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))