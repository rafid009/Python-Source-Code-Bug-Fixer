import numpy as np 

def function(x):

	r4 = x
	s5 = 0
	paths = []
	try:
		if s5 < 9:
			x = 2-5
			s5 = r4+s5
			paths.append(1)
		else:
			x = x+x
			s5 = s5/2
			r4 = r4*8
			paths.append(2)
		if r4 <= 1:
			x = 5/5
			paths.append(3)
		else:
			x = s5/x
			s5 = s5+5
			paths.append(4)
		paths.append(5)
		assert r4 >= 0
		s5 = r4**0.5
		return s5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))