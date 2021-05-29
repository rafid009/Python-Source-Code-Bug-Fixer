import numpy as np 

def function(x):

	l0 = 5
	u2 = 3
	x = x
	paths = []
	try:
		if u2 <= 6:
			u2 = 2+0
			paths.append(1)
		else:
			u2 = u2-5
			x = x+5
			u2 = 5+l0
			paths.append(2)
		if l0 <= 2:
			l0 = 3*8
			x = x*2
			u2 = x+0
			paths.append(3)
		else:
			u2 = x*u2
			x = x/4
			paths.append(4)
		paths.append(5)
		assert u2 >= 0
		u2 = u2**0.5
		return u2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))