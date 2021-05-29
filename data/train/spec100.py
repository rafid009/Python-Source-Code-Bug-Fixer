import numpy as np 

def function(x):

	u9 = 1
	s5 = x
	x = x
	paths = []
	try:
		if x < 6:
			s5 = s5+0
			s5 = s5+5
			s5 = 9/9
			paths.append(1)
		else:
			x = 2+x
			u9 = 8+u9
			s5 = 6-s5
			paths.append(2)
		if u9 < 7:
			u9 = u9/u9
			u9 = u9/6
			s5 = s5+6
			paths.append(3)
		else:
			u9 = 3-9
			u9 = u9*4
			paths.append(4)
		paths.append(5)
		assert u9 >= 0
		u9 = u9**0.5
		return u9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))