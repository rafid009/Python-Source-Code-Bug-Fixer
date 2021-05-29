import numpy as np 

def function(x):

	s7 = x
	t3 = x
	paths = []
	try:
		if t3 <= 3:
			x = x+x
			paths.append(1)
		else:
			t3 = t3-x
			t3 = x/x
			paths.append(2)
		if s7 < 2:
			s7 = s7+6
			x = x/t3
			paths.append(3)
		else:
			t3 = x/1
			x = 1+x
			paths.append(4)
		paths.append(5)
		assert t3 >= 0
		x = t3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))