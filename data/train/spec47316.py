import numpy as np 

def function(x):

	t6 = 8
	s4 = x
	paths = []
	try:
		if x >= 4:
			x = x*7
			paths.append(1)
		else:
			s4 = s4+x
			paths.append(2)
		if s4 <= 1:
			t6 = t6+0
			x = x*3
			paths.append(3)
		else:
			x = 4-x
			s4 = 4+s4
			t6 = t6/7
			paths.append(4)
		paths.append(5)
		assert s4 >= 0
		x = s4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))