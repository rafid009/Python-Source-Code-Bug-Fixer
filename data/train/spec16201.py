import numpy as np 

def function(x):

	s9 = x
	b1 = 8
	x = 0
	paths = []
	try:
		if b1 <= 4:
			b1 = s9+b1
			x = s9*x
			paths.append(1)
		else:
			b1 = 4+s9
			b1 = 4*1
			paths.append(2)
		if x < 9:
			s9 = 6+s9
			x = s9*x
			paths.append(3)
		else:
			b1 = 2-b1
			x = x+8
			paths.append(4)
		paths.append(5)
		assert s9 >= 0
		x = s9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))