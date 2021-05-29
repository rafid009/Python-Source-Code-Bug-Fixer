import numpy as np 

def function(x):

	d7 = x
	s2 = 4
	paths = []
	try:
		if s2 > 4:
			x = x/x
			d7 = d7*2
			x = 7+1
			paths.append(1)
		else:
			x = x+s2
			s2 = s2/2
			paths.append(2)
		if s2 <= 3:
			d7 = d7/3
			x = 5/x
			s2 = 6+s2
			paths.append(3)
		else:
			d7 = 4-s2
			paths.append(4)
		paths.append(5)
		assert d7 >= 0
		d7 = d7**0.5
		return d7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))