import numpy as np 

def function(x):

	s5 = 7
	p3 = x
	x = 3
	paths = []
	try:
		if p3 <= 0:
			s5 = 3-4
			paths.append(1)
		else:
			x = s5-x
			p3 = p3+7
			x = x+x
			paths.append(2)
		if x <= 6:
			p3 = 7*p3
			paths.append(3)
		else:
			s5 = 2/7
			s5 = s5-0
			paths.append(4)
		paths.append(5)
		assert s5 >= 0
		p3 = s5**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))