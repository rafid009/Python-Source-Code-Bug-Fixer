import numpy as np 

def function(x):

	s1 = 8
	u5 = x
	paths = []
	try:
		if u5 <= 3:
			s1 = u5-5
			u5 = x-2
			u5 = 0+u5
			paths.append(1)
		else:
			s1 = 5/s1
			paths.append(2)
		if x > 9:
			u5 = u5/1
			u5 = u5/6
			u5 = u5/5
			paths.append(3)
		else:
			s1 = 1+s1
			s1 = s1*9
			u5 = s1*x
			paths.append(4)
		paths.append(5)
		assert u5 >= 0
		s1 = u5**0.5
		return s1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))