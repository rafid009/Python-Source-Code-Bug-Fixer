import numpy as np 

def function(x):

	i9 = x
	s5 = x
	paths = []
	try:
		if i9 <= 7:
			i9 = i9-s5
			paths.append(1)
		else:
			i9 = i9-3
			i9 = x/i9
			s5 = 2/s5
			paths.append(2)
		if x < 0:
			i9 = 5-i9
			paths.append(3)
		else:
			x = s5+s5
			x = x*0
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