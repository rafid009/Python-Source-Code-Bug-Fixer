import numpy as np 

def function(x):

	s5 = 9
	b9 = 5
	paths = []
	try:
		if s5 > 3:
			b9 = s5+b9
			x = x*2
			x = 1-x
			paths.append(1)
		else:
			b9 = 4-0
			s5 = 4-s5
			s5 = 9+s5
			paths.append(2)
		if s5 >= 3:
			b9 = b9-7
			s5 = 4-s5
			paths.append(3)
		else:
			x = 1+9
			b9 = 9-b9
			s5 = s5-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))