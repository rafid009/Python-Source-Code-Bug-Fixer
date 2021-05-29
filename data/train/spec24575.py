import numpy as np 

def function(x):

	b7 = x
	u3 = x
	paths = []
	try:
		if u3 < 6:
			x = 2*x
			b7 = 9-0
			x = x-x
			paths.append(1)
		else:
			b7 = b7+u3
			x = 9/x
			u3 = 7-u3
			paths.append(2)
		if x < 3:
			x = x*2
			x = 3-x
			x = x+9
			paths.append(3)
		else:
			u3 = x+8
			b7 = x*u3
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		b7 = u3**0.5
		return b7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))