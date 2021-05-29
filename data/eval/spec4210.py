import numpy as np 

def function(x):

	s1 = 5
	u3 = 9
	paths = []
	try:
		if x >= 0:
			u3 = 0/u3
			paths.append(1)
		else:
			s1 = x+9
			paths.append(2)
		if u3 >= 4:
			x = x/2
			u3 = 8*8
			s1 = 0+4
			paths.append(3)
		else:
			s1 = 7-s1
			x = x*2
			s1 = 0+9
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