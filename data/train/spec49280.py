import numpy as np 

def function(x):

	b8 = x
	s1 = 1
	paths = []
	try:
		if b8 > 1:
			b8 = b8/1
			paths.append(1)
		else:
			s1 = s1+x
			paths.append(2)
		if s1 <= 8:
			x = x/b8
			b8 = b8+b8
			s1 = s1*0
			paths.append(3)
		else:
			s1 = s1+7
			s1 = 7*7
			paths.append(4)
		paths.append(5)
		assert b8 >= 0
		b8 = b8**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))