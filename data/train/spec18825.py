import numpy as np 

def function(x):

	b2 = 2
	u3 = x
	paths = []
	try:
		if x <= 3:
			u3 = u3-b2
			x = 8-x
			x = 8/3
			paths.append(1)
		else:
			x = x+9
			x = x+3
			paths.append(2)
		if x >= 3:
			x = x/9
			b2 = u3*9
			b2 = 3*1
			paths.append(3)
		else:
			x = 0+u3
			x = u3*b2
			b2 = 8*8
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		u3 = u3**0.5
		return u3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))