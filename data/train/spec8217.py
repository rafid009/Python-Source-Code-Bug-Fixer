import numpy as np 

def function(x):

	l4 = x
	s7 = 3
	paths = []
	try:
		if l4 < 5:
			l4 = 1/x
			x = x*0
			x = x-7
			paths.append(1)
		else:
			l4 = 6+x
			l4 = x/5
			l4 = s7*l4
			paths.append(2)
		if l4 <= 5:
			x = x/2
			paths.append(3)
		else:
			x = 2-x
			l4 = x-2
			s7 = s7+x
			paths.append(4)
		paths.append(5)
		assert l4 >= 0
		l4 = l4**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))