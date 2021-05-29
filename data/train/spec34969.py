import numpy as np 

def function(x):

	u1 = x
	e5 = x
	x = 5
	paths = []
	try:
		if u1 <= 3:
			x = 2/8
			e5 = e5*5
			u1 = u1+x
			paths.append(1)
		else:
			e5 = x+e5
			x = 7*0
			x = x-5
			paths.append(2)
		if x >= 3:
			u1 = e5+e5
			paths.append(3)
		else:
			x = u1-4
			paths.append(4)
		paths.append(5)
		assert u1 >= 0
		e5 = u1**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))