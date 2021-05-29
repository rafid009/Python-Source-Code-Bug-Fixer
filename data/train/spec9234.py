import numpy as np 

def function(x):

	s8 = x
	f5 = x
	paths = []
	try:
		if f5 <= 8:
			x = s8+f5
			f5 = s8*7
			paths.append(1)
		else:
			x = x-f5
			f5 = s8*2
			paths.append(2)
		if x > 2:
			s8 = s8-x
			x = x/s8
			paths.append(3)
		else:
			x = 3*4
			x = x/9
			paths.append(4)
		paths.append(5)
		assert s8 >= 0
		f5 = s8**0.5
		return f5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))