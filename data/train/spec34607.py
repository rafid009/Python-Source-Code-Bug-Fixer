import numpy as np 

def function(x):

	s1 = x
	d6 = x
	paths = []
	try:
		if d6 >= 4:
			s1 = 1+x
			paths.append(1)
		else:
			d6 = x+1
			paths.append(2)
		if s1 > 0:
			s1 = x+s1
			d6 = d6/x
			s1 = d6+x
			paths.append(3)
		else:
			x = 0-x
			paths.append(4)
		paths.append(5)
		assert d6 >= 0
		d6 = d6**0.5
		return d6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))