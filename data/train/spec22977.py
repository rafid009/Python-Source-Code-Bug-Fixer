import numpy as np 

def function(x):

	s4 = 6
	l4 = x
	paths = []
	try:
		if x < 9:
			s4 = 4-s4
			l4 = 6+x
			paths.append(1)
		else:
			l4 = x*x
			x = l4+x
			s4 = x+s4
			paths.append(2)
		if x > 7:
			l4 = l4*0
			x = 1/8
			paths.append(3)
		else:
			s4 = s4/8
			paths.append(4)
		paths.append(5)
		assert l4 >= 0
		x = l4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))