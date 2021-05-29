import numpy as np 

def function(x):

	p9 = x
	s1 = x
	x = 4
	paths = []
	try:
		if p9 > 7:
			p9 = 9+7
			x = x-3
			paths.append(1)
		else:
			s1 = s1*s1
			paths.append(2)
		if p9 >= 0:
			x = x*p9
			paths.append(3)
		else:
			s1 = s1+s1
			s1 = p9*0
			paths.append(4)
		paths.append(5)
		assert p9 >= 0
		s1 = p9**0.5
		return s1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))