import numpy as np 

def function(x):

	d6 = x
	s5 = x
	paths = []
	try:
		if s5 < 1:
			s5 = 9-s5
			x = 7*7
			paths.append(1)
		else:
			x = s5-x
			s5 = 6-s5
			paths.append(2)
		if s5 < 0:
			d6 = 4+1
			d6 = d6-s5
			paths.append(3)
		else:
			s5 = s5-9
			d6 = d6+x
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