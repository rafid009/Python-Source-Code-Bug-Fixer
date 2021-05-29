import numpy as np 

def function(x):

	n6 = x
	s9 = x
	paths = []
	try:
		if s9 >= 4:
			x = x+1
			paths.append(1)
		else:
			n6 = n6*9
			paths.append(2)
		if n6 <= 7:
			s9 = 7-5
			x = x/9
			n6 = n6*x
			paths.append(3)
		else:
			x = x*0
			s9 = s9*5
			s9 = s9*n6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))