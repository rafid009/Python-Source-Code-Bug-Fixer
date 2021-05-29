import numpy as np 

def function(x):

	b1 = x
	s7 = 1
	paths = []
	try:
		if b1 >= 5:
			x = 2/1
			paths.append(1)
		else:
			x = 9+x
			paths.append(2)
		if b1 < 2:
			s7 = 2/b1
			s7 = s7+1
			s7 = s7+0
			paths.append(3)
		else:
			s7 = s7+x
			b1 = b1*5
			x = x+b1
			paths.append(4)
		paths.append(5)
		assert s7 >= 0
		b1 = s7**0.5
		return b1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))