import numpy as np 

def function(x):

	p6 = 5
	s8 = 8
	x = 2
	paths = []
	try:
		if x < 0:
			p6 = p6+0
			p6 = p6+2
			x = p6/8
			paths.append(1)
		else:
			x = 5-x
			p6 = 4-p6
			paths.append(2)
		if x > 3:
			p6 = 5*9
			paths.append(3)
		else:
			s8 = x*7
			s8 = 8*2
			s8 = p6/2
			paths.append(4)
		paths.append(5)
		assert p6 >= 0
		p6 = p6**0.5
		return p6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))