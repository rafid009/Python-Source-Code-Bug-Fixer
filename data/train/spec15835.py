import numpy as np 

def function(x):

	b5 = x
	s1 = x
	x = 3
	paths = []
	try:
		if b5 > 1:
			b5 = 4-b5
			paths.append(1)
		else:
			x = x-4
			x = x/7
			s1 = s1-4
			paths.append(2)
		if x >= 7:
			x = s1+x
			paths.append(3)
		else:
			s1 = 9/6
			paths.append(4)
		paths.append(5)
		assert b5 >= 0
		b5 = b5**0.5
		return b5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))