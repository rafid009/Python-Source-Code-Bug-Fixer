import numpy as np 

def function(x):

	s9 = x
	p4 = 2
	x = 5
	paths = []
	try:
		if p4 < 5:
			x = x*p4
			p4 = 4-s9
			p4 = 8-s9
			paths.append(1)
		else:
			x = 6-5
			x = x*s9
			s9 = 2+s9
			paths.append(2)
		if s9 <= 0:
			p4 = 9+x
			paths.append(3)
		else:
			p4 = p4+p4
			p4 = p4*1
			s9 = 6+s9
			paths.append(4)
		paths.append(5)
		assert p4 >= 0
		x = p4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))