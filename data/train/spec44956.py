import numpy as np 

def function(x):

	b8 = 7
	s2 = 9
	x = x
	paths = []
	try:
		if s2 >= 2:
			s2 = b8-2
			b8 = b8*b8
			paths.append(1)
		else:
			x = b8/x
			x = s2+9
			b8 = b8+1
			paths.append(2)
		if x < 7:
			b8 = b8*0
			s2 = b8*x
			paths.append(3)
		else:
			b8 = s2+b8
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