import numpy as np 

def function(x):

	s5 = 1
	b1 = x
	paths = []
	try:
		if s5 <= 3:
			b1 = 4/b1
			s5 = b1*s5
			paths.append(1)
		else:
			s5 = s5/x
			paths.append(2)
		if x > 1:
			x = 7-3
			paths.append(3)
		else:
			b1 = 5/b1
			x = x+b1
			paths.append(4)
		paths.append(5)
		assert b1 >= 0
		x = b1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))