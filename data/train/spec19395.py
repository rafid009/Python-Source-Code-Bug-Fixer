import numpy as np 

def function(x):

	s8 = x
	p6 = x
	paths = []
	try:
		if p6 <= 7:
			s8 = p6/p6
			p6 = p6-1
			paths.append(1)
		else:
			s8 = 2/s8
			paths.append(2)
		if x <= 8:
			x = x+s8
			p6 = p6+1
			paths.append(3)
		else:
			x = s8+x
			s8 = s8+6
			paths.append(4)
		paths.append(5)
		assert p6 >= 0
		x = p6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))