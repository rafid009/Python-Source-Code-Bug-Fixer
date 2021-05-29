import numpy as np 

def function(x):

	b9 = x
	u1 = x
	paths = []
	try:
		if u1 <= 3:
			b9 = 8/x
			u1 = u1*9
			paths.append(1)
		else:
			u1 = x+u1
			b9 = 8+x
			x = 1+5
			paths.append(2)
		if b9 >= 0:
			x = 7/x
			b9 = b9-2
			x = x+4
			paths.append(3)
		else:
			b9 = u1/b9
			x = x/x
			u1 = u1/8
			paths.append(4)
		paths.append(5)
		assert u1 >= 0
		u1 = u1**0.5
		return u1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))