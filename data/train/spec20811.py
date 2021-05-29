import numpy as np 

def function(x):

	s5 = x
	p1 = 7
	paths = []
	try:
		if s5 <= 7:
			s5 = x*4
			p1 = 7*1
			paths.append(1)
		else:
			s5 = 1+4
			s5 = s5-6
			p1 = 2-5
			paths.append(2)
		if x <= 7:
			p1 = 3-p1
			x = x*p1
			s5 = 0*2
			paths.append(3)
		else:
			p1 = 8+7
			paths.append(4)
		paths.append(5)
		assert p1 >= 0
		x = p1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))