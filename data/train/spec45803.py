import numpy as np 

def function(x):

	d6 = x
	s1 = 5
	x = x
	paths = []
	try:
		if d6 <= 4:
			x = d6-5
			paths.append(1)
		else:
			s1 = d6+5
			d6 = 8+4
			s1 = d6-s1
			paths.append(2)
		if s1 > 6:
			s1 = 2/x
			d6 = x*s1
			s1 = x+s1
			paths.append(3)
		else:
			s1 = s1-0
			paths.append(4)
		paths.append(5)
		assert s1 >= 0
		x = s1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))