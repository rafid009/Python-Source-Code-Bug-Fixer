import numpy as np 

def function(x):

	s5 = 3
	b0 = x
	x = x
	paths = []
	try:
		if s5 < 5:
			b0 = b0+x
			x = 3+b0
			paths.append(1)
		else:
			b0 = b0*1
			b0 = b0-9
			b0 = b0-1
			paths.append(2)
		if x >= 4:
			s5 = s5-6
			x = b0+1
			b0 = s5*b0
			paths.append(3)
		else:
			x = 0+x
			s5 = x*s5
			paths.append(4)
		paths.append(5)
		assert s5 >= 0
		x = s5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))