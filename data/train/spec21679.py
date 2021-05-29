import numpy as np 

def function(x):

	s1 = 2
	d7 = 5
	paths = []
	try:
		if x < 2:
			x = d7-x
			paths.append(1)
		else:
			x = x/2
			s1 = 0*s1
			s1 = s1/6
			paths.append(2)
		if d7 <= 7:
			s1 = s1-9
			x = d7+x
			x = x+x
			paths.append(3)
		else:
			d7 = s1+s1
			d7 = d7*1
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