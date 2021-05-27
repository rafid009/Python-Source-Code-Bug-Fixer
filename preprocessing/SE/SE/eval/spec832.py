import numpy as np 

def function(x):

	u9 = x
	s5 = x
	paths = []
	try:
		if x >= 4:
			x = s5+x
			s5 = s5-2
			paths.append(1)
		else:
			s5 = s5*1
			s5 = 2+x
			u9 = u9*u9
			paths.append(2)
		if x < 5:
			s5 = s5+2
			s5 = 4/s5
			x = x-u9
			paths.append(3)
		else:
			s5 = s5-5
			u9 = x/8
			s5 = s5*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u9 = x**0.5
		return u9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))