import numpy as np 

def function(x):

	s5 = x
	x2 = 8
	x = x
	paths = []
	try:
		if x2 > 5:
			s5 = 6/s5
			x = x-2
			paths.append(1)
		else:
			s5 = 0*0
			paths.append(2)
		if s5 >= 1:
			x2 = 8*s5
			x2 = 6+x2
			x2 = x2/1
			paths.append(3)
		else:
			x = s5*2
			paths.append(4)
		paths.append(5)
		assert s5 >= 0
		x2 = s5**0.5
		return x2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))