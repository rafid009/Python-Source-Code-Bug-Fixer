import numpy as np 

def function(x):

	r9 = x
	u1 = 3
	paths = []
	try:
		if x <= 6:
			u1 = u1+9
			r9 = r9+r9
			u1 = 9*x
			paths.append(1)
		else:
			x = x-x
			r9 = r9/2
			paths.append(2)
		if u1 <= 4:
			r9 = r9+1
			x = x*r9
			paths.append(3)
		else:
			x = x+7
			r9 = r9-5
			paths.append(4)
		paths.append(5)
		assert r9 >= 0
		u1 = r9**0.5
		return u1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))