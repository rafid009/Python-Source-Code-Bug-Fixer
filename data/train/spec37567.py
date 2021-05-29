import numpy as np 

def function(x):

	s2 = x
	v7 = 4
	x = x
	paths = []
	try:
		if x > 7:
			x = 7*x
			x = 8*4
			x = x+0
			paths.append(1)
		else:
			s2 = 5*0
			v7 = 9+v7
			v7 = v7-v7
			paths.append(2)
		if s2 <= 1:
			s2 = s2-6
			paths.append(3)
		else:
			x = x*2
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