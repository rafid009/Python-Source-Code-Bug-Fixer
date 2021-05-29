import numpy as np 

def function(x):

	s1 = 2
	n8 = x
	paths = []
	try:
		if s1 > 6:
			x = s1/6
			s1 = s1+2
			paths.append(1)
		else:
			s1 = n8+s1
			n8 = n8-7
			n8 = x*7
			paths.append(2)
		if n8 >= 9:
			n8 = n8+5
			n8 = 4/s1
			n8 = n8/6
			paths.append(3)
		else:
			s1 = s1+s1
			paths.append(4)
		paths.append(5)
		assert s1 >= 0
		n8 = s1**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))