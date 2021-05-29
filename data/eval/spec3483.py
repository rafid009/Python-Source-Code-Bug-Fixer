import numpy as np 

def function(x):

	s1 = x
	b3 = x
	paths = []
	try:
		if x <= 5:
			s1 = s1/5
			paths.append(1)
		else:
			s1 = s1*8
			paths.append(2)
		if x > 4:
			s1 = x*s1
			x = b3*7
			s1 = 4/b3
			paths.append(3)
		else:
			x = x/x
			b3 = b3-s1
			x = x*0
			paths.append(4)
		paths.append(5)
		assert b3 >= 0
		s1 = b3**0.5
		return s1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))