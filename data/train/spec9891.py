import numpy as np 

def function(x):

	p1 = x
	s5 = 1
	paths = []
	try:
		if p1 <= 7:
			x = 2/3
			paths.append(1)
		else:
			x = 8-x
			p1 = p1*1
			paths.append(2)
		if x >= 7:
			p1 = p1-1
			x = 7-x
			x = x-3
			paths.append(3)
		else:
			x = 2*6
			s5 = s5+s5
			paths.append(4)
		paths.append(5)
		assert p1 >= 0
		p1 = p1**0.5
		return p1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))