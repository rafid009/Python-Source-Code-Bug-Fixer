import numpy as np 

def function(x):

	l1 = x
	s9 = x
	paths = []
	try:
		if l1 <= 6:
			l1 = x*l1
			s9 = 3+s9
			paths.append(1)
		else:
			x = 6+s9
			paths.append(2)
		if x < 9:
			l1 = l1-2
			l1 = 2-7
			s9 = x*l1
			paths.append(3)
		else:
			x = x-8
			x = x-l1
			paths.append(4)
		paths.append(5)
		assert s9 >= 0
		l1 = s9**0.5
		return l1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))