import numpy as np 

def function(x):

	n4 = x
	s5 = x
	x = 4
	paths = []
	try:
		if x <= 6:
			x = 4*9
			x = x*s5
			x = 5/n4
			paths.append(1)
		else:
			n4 = s5*6
			paths.append(2)
		if n4 < 7:
			x = x*1
			paths.append(3)
		else:
			s5 = n4+5
			n4 = n4*5
			paths.append(4)
		paths.append(5)
		assert s5 >= 0
		n4 = s5**0.5
		return n4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))