import numpy as np 

def function(x):

	d5 = x
	s8 = x
	paths = []
	try:
		if d5 <= 7:
			s8 = s8*7
			x = x+s8
			d5 = 6-d5
			paths.append(1)
		else:
			x = 2*x
			x = x/x
			d5 = d5/1
			paths.append(2)
		if x < 1:
			s8 = x*0
			paths.append(3)
		else:
			x = d5*x
			paths.append(4)
		paths.append(5)
		assert d5 >= 0
		x = d5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))