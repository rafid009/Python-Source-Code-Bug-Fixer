import numpy as np 

def function(x):

	s2 = 8
	b1 = x
	paths = []
	try:
		if b1 <= 6:
			b1 = 7-b1
			s2 = s2/8
			paths.append(1)
		else:
			s2 = s2/9
			paths.append(2)
		if b1 <= 5:
			s2 = s2-1
			paths.append(3)
		else:
			b1 = 3+x
			paths.append(4)
		paths.append(5)
		assert b1 >= 0
		b1 = b1**0.5
		return b1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))