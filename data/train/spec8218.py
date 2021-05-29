import numpy as np 

def function(x):

	p7 = x
	s2 = 7
	paths = []
	try:
		if s2 > 3:
			x = x*4
			paths.append(1)
		else:
			p7 = 4-7
			paths.append(2)
		if p7 < 5:
			x = x-5
			s2 = p7*5
			s2 = 2/5
			paths.append(3)
		else:
			x = 0+x
			s2 = x+1
			p7 = 3/7
			paths.append(4)
		paths.append(5)
		assert p7 >= 0
		x = p7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))