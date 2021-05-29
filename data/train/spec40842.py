import numpy as np 

def function(x):

	s2 = x
	k6 = 0
	paths = []
	try:
		if k6 < 8:
			x = x+1
			k6 = x/x
			paths.append(1)
		else:
			s2 = 3*0
			s2 = 8+1
			k6 = k6+s2
			paths.append(2)
		if k6 >= 0:
			k6 = 8/k6
			k6 = 4-0
			k6 = k6+k6
			paths.append(3)
		else:
			k6 = k6*1
			k6 = k6/8
			x = 4/x
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