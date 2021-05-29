import numpy as np 

def function(x):

	d9 = 3
	s5 = x
	paths = []
	try:
		if d9 <= 9:
			x = 6+x
			s5 = 5-s5
			paths.append(1)
		else:
			s5 = 4-s5
			s5 = 3-s5
			d9 = d9*0
			paths.append(2)
		if s5 > 1:
			d9 = 4+s5
			paths.append(3)
		else:
			s5 = s5*d9
			x = 4+x
			x = x-s5
			paths.append(4)
		paths.append(5)
		assert s5 >= 0
		x = s5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))