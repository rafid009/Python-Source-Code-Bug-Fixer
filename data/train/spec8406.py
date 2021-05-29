import numpy as np 

def function(x):

	s1 = x
	m3 = x
	paths = []
	try:
		if x > 5:
			x = s1+x
			x = x-7
			s1 = s1*s1
			paths.append(1)
		else:
			s1 = s1-2
			paths.append(2)
		if s1 <= 7:
			m3 = 7/m3
			x = 1+7
			paths.append(3)
		else:
			x = 9/x
			s1 = 4/7
			m3 = 0+m3
			paths.append(4)
		paths.append(5)
		assert s1 >= 0
		s1 = s1**0.5
		return s1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))