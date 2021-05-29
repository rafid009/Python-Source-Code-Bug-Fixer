import numpy as np 

def function(x):

	w1 = x
	s1 = x
	paths = []
	try:
		if x >= 8:
			w1 = w1+w1
			s1 = 5/4
			paths.append(1)
		else:
			x = x*5
			x = x/s1
			paths.append(2)
		if x > 4:
			w1 = 1*1
			s1 = 1-s1
			paths.append(3)
		else:
			x = x*0
			s1 = s1+9
			s1 = 0+w1
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