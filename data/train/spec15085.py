import numpy as np 

def function(x):

	s5 = x
	b6 = 2
	paths = []
	try:
		if b6 > 2:
			b6 = 5+x
			x = s5*2
			b6 = b6+0
			paths.append(1)
		else:
			x = x*b6
			x = x*9
			paths.append(2)
		if x >= 3:
			b6 = b6-2
			s5 = s5+x
			paths.append(3)
		else:
			b6 = b6+b6
			b6 = b6+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b6 = x**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))