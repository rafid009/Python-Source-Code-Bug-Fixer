import numpy as np 

def function(x):

	f3 = 3
	u1 = 7
	paths = []
	try:
		if f3 < 2:
			f3 = x+f3
			x = 0+x
			u1 = u1*3
			paths.append(1)
		else:
			x = x-u1
			u1 = 3-6
			paths.append(2)
		if u1 >= 0:
			x = 6/f3
			x = 2+x
			paths.append(3)
		else:
			f3 = f3+x
			paths.append(4)
		paths.append(5)
		assert f3 >= 0
		u1 = f3**0.5
		return u1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))