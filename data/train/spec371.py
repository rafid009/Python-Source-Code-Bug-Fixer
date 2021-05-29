import numpy as np 

def function(x):

	t3 = x
	s7 = 7
	paths = []
	try:
		if s7 > 4:
			s7 = s7/s7
			paths.append(1)
		else:
			x = 0*6
			x = 0/x
			paths.append(2)
		if x <= 1:
			s7 = s7-t3
			x = t3+7
			t3 = t3+8
			paths.append(3)
		else:
			t3 = 7*7
			x = x/1
			x = x*8
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