import numpy as np 

def function(x):

	u3 = 1
	f7 = 2
	paths = []
	try:
		if x < 9:
			u3 = 4/u3
			u3 = x*u3
			paths.append(1)
		else:
			x = 3/x
			f7 = 0*8
			paths.append(2)
		if u3 <= 3:
			f7 = 9/6
			u3 = u3*u3
			x = 0+x
			paths.append(3)
		else:
			u3 = u3-9
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