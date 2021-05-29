import numpy as np 

def function(x):

	s5 = x
	t3 = x
	paths = []
	try:
		if s5 > 2:
			s5 = s5+4
			paths.append(1)
		else:
			s5 = t3+t3
			paths.append(2)
		if x <= 1:
			x = 9*x
			s5 = s5+t3
			paths.append(3)
		else:
			t3 = 8*7
			s5 = x/s5
			s5 = t3+2
			paths.append(4)
		paths.append(5)
		assert t3 >= 0
		t3 = t3**0.5
		return t3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))