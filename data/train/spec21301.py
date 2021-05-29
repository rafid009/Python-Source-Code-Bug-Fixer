import numpy as np 

def function(x):

	p2 = x
	s6 = 2
	paths = []
	try:
		if p2 < 4:
			x = s6*1
			x = x/6
			paths.append(1)
		else:
			s6 = s6*0
			paths.append(2)
		if x > 6:
			x = x+s6
			paths.append(3)
		else:
			s6 = p2+4
			s6 = 0*7
			x = x-2
			paths.append(4)
		paths.append(5)
		assert p2 >= 0
		s6 = p2**0.5
		return s6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))