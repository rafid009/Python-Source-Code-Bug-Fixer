import numpy as np 

def function(x):

	b9 = x
	s7 = 1
	paths = []
	try:
		if b9 > 6:
			x = x*5
			b9 = b9*3
			paths.append(1)
		else:
			x = x+1
			s7 = 6+0
			x = x+x
			paths.append(2)
		if x < 0:
			x = s7*x
			b9 = 6/b9
			paths.append(3)
		else:
			b9 = b9/s7
			s7 = s7-4
			paths.append(4)
		paths.append(5)
		assert b9 >= 0
		b9 = b9**0.5
		return b9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))