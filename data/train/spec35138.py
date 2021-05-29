import numpy as np 

def function(x):

	s5 = 9
	p6 = x
	paths = []
	try:
		if p6 >= 3:
			p6 = p6*1
			p6 = p6*5
			paths.append(1)
		else:
			x = x*5
			p6 = 3+1
			s5 = 6-0
			paths.append(2)
		if x <= 7:
			p6 = 0-2
			p6 = 1+p6
			paths.append(3)
		else:
			x = x+7
			paths.append(4)
		paths.append(5)
		assert p6 >= 0
		x = p6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))