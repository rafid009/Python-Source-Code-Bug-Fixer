import numpy as np 

def function(x):

	s8 = 7
	b1 = 2
	x = 0
	paths = []
	try:
		if x >= 6:
			b1 = 7*b1
			paths.append(1)
		else:
			s8 = s8+5
			s8 = 8-s8
			b1 = s8-s8
			paths.append(2)
		if b1 <= 2:
			x = s8*7
			paths.append(3)
		else:
			b1 = x/b1
			b1 = s8*b1
			x = x*9
			paths.append(4)
		paths.append(5)
		assert s8 >= 0
		b1 = s8**0.5
		return b1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))