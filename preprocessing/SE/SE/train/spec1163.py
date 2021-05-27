import numpy as np 

def function(x):

	s1 = 5
	i5 = x
	x = 8
	paths = []
	try:
		if x <= 9:
			s1 = s1/x
			i5 = 6+i5
			paths.append(1)
		else:
			i5 = i5-4
			paths.append(2)
		if x > 4:
			s1 = 0-8
			s1 = 9*0
			paths.append(3)
		else:
			x = x+s1
			s1 = i5+3
			s1 = s1+4
			paths.append(4)
		paths.append(5)
		assert i5 >= 0
		s1 = i5**0.5
		return s1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))