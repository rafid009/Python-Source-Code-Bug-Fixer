import numpy as np 

def function(x):

	d1 = 5
	s5 = x
	paths = []
	try:
		if x > 2:
			s5 = x-s5
			d1 = s5/x
			d1 = x*6
			paths.append(1)
		else:
			x = 3/x
			d1 = d1+d1
			paths.append(2)
		if d1 <= 5:
			x = s5*3
			paths.append(3)
		else:
			d1 = d1*9
			paths.append(4)
		paths.append(5)
		assert s5 >= 0
		d1 = s5**0.5
		return d1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))