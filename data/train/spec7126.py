import numpy as np 

def function(x):

	p9 = 7
	s2 = x
	paths = []
	try:
		if p9 > 6:
			x = s2-0
			s2 = x-7
			paths.append(1)
		else:
			p9 = 7/p9
			p9 = x/4
			paths.append(2)
		if s2 <= 4:
			p9 = 3+5
			paths.append(3)
		else:
			s2 = s2*4
			x = x/2
			p9 = p9*0
			paths.append(4)
		paths.append(5)
		assert s2 >= 0
		s2 = s2**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))