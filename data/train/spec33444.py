import numpy as np 

def function(x):

	s2 = x
	u6 = 6
	paths = []
	try:
		if x > 5:
			u6 = 4*6
			s2 = 4-7
			u6 = s2+s2
			paths.append(1)
		else:
			s2 = s2-0
			s2 = 1/s2
			x = 4/1
			paths.append(2)
		if u6 > 4:
			s2 = s2+2
			x = 6-x
			paths.append(3)
		else:
			s2 = 2*s2
			s2 = s2*8
			paths.append(4)
		paths.append(5)
		assert s2 >= 0
		u6 = s2**0.5
		return u6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))