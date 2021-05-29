import numpy as np 

def function(x):

	f7 = x
	s6 = x
	paths = []
	try:
		if f7 >= 5:
			x = 8-s6
			x = x/6
			f7 = 8*7
			paths.append(1)
		else:
			x = 8+x
			s6 = s6*0
			paths.append(2)
		if x >= 4:
			x = 1+f7
			paths.append(3)
		else:
			x = 3+0
			paths.append(4)
		paths.append(5)
		assert f7 >= 0
		x = f7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))