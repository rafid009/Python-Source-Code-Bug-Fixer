import numpy as np 

def function(x):

	k5 = 8
	u2 = x
	paths = []
	try:
		if x < 3:
			x = x*1
			u2 = u2+4
			x = 9/x
			paths.append(1)
		else:
			u2 = u2+x
			x = 2*x
			x = x+6
			paths.append(2)
		if u2 <= 8:
			u2 = u2/3
			k5 = 6/k5
			paths.append(3)
		else:
			u2 = 5+k5
			k5 = 9*k5
			k5 = 7*8
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