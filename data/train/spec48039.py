import numpy as np 

def function(x):

	i5 = x
	s6 = 4
	paths = []
	try:
		if i5 > 5:
			i5 = i5*0
			paths.append(1)
		else:
			x = x+8
			i5 = i5+i5
			paths.append(2)
		if x >= 9:
			s6 = x+s6
			x = 8+0
			s6 = s6-0
			paths.append(3)
		else:
			s6 = i5-x
			paths.append(4)
		paths.append(5)
		assert s6 >= 0
		x = s6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))