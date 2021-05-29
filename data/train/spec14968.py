import numpy as np 

def function(x):

	p6 = 2
	y2 = 2
	paths = []
	try:
		if y2 > 3:
			y2 = y2*y2
			p6 = p6*0
			paths.append(1)
		else:
			p6 = 8-p6
			p6 = 3-p6
			paths.append(2)
		if x < 1:
			y2 = p6*p6
			y2 = y2/x
			x = 0/9
			paths.append(3)
		else:
			x = 2/x
			y2 = p6+y2
			paths.append(4)
		paths.append(5)
		assert y2 >= 0
		p6 = y2**0.5
		return p6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))