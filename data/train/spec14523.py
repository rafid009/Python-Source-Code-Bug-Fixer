import numpy as np 

def function(x):

	t3 = 2
	s4 = x
	paths = []
	try:
		if x < 6:
			t3 = x*3
			x = 8+3
			paths.append(1)
		else:
			s4 = 7*9
			x = s4*8
			t3 = s4+t3
			paths.append(2)
		if t3 <= 0:
			x = s4+x
			t3 = 5/3
			paths.append(3)
		else:
			t3 = t3-8
			x = 7/x
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