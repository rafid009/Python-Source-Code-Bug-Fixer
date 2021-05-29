import numpy as np 

def function(x):

	s5 = 4
	k4 = x
	x = x
	paths = []
	try:
		if x <= 1:
			x = x*8
			k4 = k4+s5
			paths.append(1)
		else:
			s5 = s5-x
			k4 = x*9
			k4 = 1+k4
			paths.append(2)
		if k4 >= 5:
			k4 = 8+1
			x = x+3
			paths.append(3)
		else:
			x = x+s5
			k4 = 0-6
			s5 = s5-k4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k4 = x**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))