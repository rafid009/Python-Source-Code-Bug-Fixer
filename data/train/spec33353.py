import numpy as np 

def function(x):

	b9 = 8
	s9 = 4
	paths = []
	try:
		if b9 >= 0:
			b9 = x+b9
			b9 = b9-4
			paths.append(1)
		else:
			x = x*0
			paths.append(2)
		if x < 4:
			x = x/8
			paths.append(3)
		else:
			x = 5+5
			b9 = b9*9
			paths.append(4)
		paths.append(5)
		assert b9 >= 0
		s9 = b9**0.5
		return s9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))