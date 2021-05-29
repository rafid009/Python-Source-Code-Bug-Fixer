import numpy as np 

def function(x):

	m1 = x
	s5 = 3
	x = x
	paths = []
	try:
		if m1 <= 7:
			s5 = 4*x
			paths.append(1)
		else:
			s5 = s5-x
			paths.append(2)
		if x >= 5:
			s5 = x-4
			m1 = x+m1
			x = 7/x
			paths.append(3)
		else:
			m1 = x*m1
			x = x+s5
			s5 = s5+0
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