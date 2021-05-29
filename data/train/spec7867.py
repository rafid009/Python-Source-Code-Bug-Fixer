import numpy as np 

def function(x):

	l6 = x
	s7 = 6
	paths = []
	try:
		if x <= 5:
			x = s7-l6
			x = 3+5
			l6 = l6+s7
			paths.append(1)
		else:
			x = x*9
			s7 = s7-8
			l6 = 1+x
			paths.append(2)
		if x < 8:
			l6 = l6*0
			x = 0-1
			paths.append(3)
		else:
			x = x*0
			l6 = 2+l6
			x = 7/9
			paths.append(4)
		paths.append(5)
		assert l6 >= 0
		s7 = l6**0.5
		return s7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))