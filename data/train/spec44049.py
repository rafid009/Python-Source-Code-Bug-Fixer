import numpy as np 

def function(x):

	u3 = 2
	l4 = 4
	paths = []
	try:
		if x < 5:
			u3 = u3-8
			x = 4-5
			l4 = l4*x
			paths.append(1)
		else:
			l4 = l4/2
			u3 = l4-u3
			x = x-7
			paths.append(2)
		if u3 > 3:
			x = x*l4
			l4 = l4*8
			x = 8/l4
			paths.append(3)
		else:
			l4 = u3*l4
			x = x/6
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		x = u3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))