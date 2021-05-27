import numpy as np 

def function(x):

	p1 = x
	s2 = 6
	paths = []
	try:
		if p1 > 1:
			x = x*x
			paths.append(1)
		else:
			x = 7*x
			s2 = p1-6
			s2 = x*s2
			paths.append(2)
		if p1 <= 0:
			p1 = 7*p1
			x = 9+x
			paths.append(3)
		else:
			p1 = p1+x
			x = x/8
			p1 = 0*0
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