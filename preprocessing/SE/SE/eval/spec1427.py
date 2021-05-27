import numpy as np 

def function(x):

	s5 = 7
	i1 = 0
	paths = []
	try:
		if i1 < 9:
			x = x-7
			s5 = x-4
			x = x-i1
			paths.append(1)
		else:
			i1 = 9+x
			paths.append(2)
		if x < 1:
			x = x*0
			i1 = s5-8
			paths.append(3)
		else:
			x = 6/s5
			paths.append(4)
		paths.append(5)
		assert i1 >= 0
		s5 = i1**0.5
		return s5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))