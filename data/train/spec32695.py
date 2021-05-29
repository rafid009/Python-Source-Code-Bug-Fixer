import numpy as np 

def function(x):

	s5 = 9
	f3 = x
	paths = []
	try:
		if x > 5:
			s5 = s5/2
			f3 = f3-4
			s5 = s5-0
			paths.append(1)
		else:
			x = 9+x
			x = x+8
			paths.append(2)
		if x >= 0:
			f3 = s5+f3
			x = x-5
			paths.append(3)
		else:
			f3 = f3-f3
			paths.append(4)
		paths.append(5)
		assert f3 >= 0
		f3 = f3**0.5
		return f3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))