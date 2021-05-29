import numpy as np 

def function(x):

	s5 = x
	i5 = 9
	paths = []
	try:
		if i5 >= 7:
			x = x*0
			x = 4*s5
			s5 = 6*9
			paths.append(1)
		else:
			x = x+s5
			x = 6/x
			paths.append(2)
		if x <= 3:
			i5 = 0+6
			x = s5/x
			x = 5-x
			paths.append(3)
		else:
			s5 = 0/s5
			i5 = 2+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i5 = x**0.5
		return i5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))