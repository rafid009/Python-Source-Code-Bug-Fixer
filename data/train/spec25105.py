import numpy as np 

def function(x):

	r8 = x
	u3 = 1
	paths = []
	try:
		if x <= 8:
			x = x*3
			r8 = 2*r8
			paths.append(1)
		else:
			x = x+r8
			x = 3-x
			u3 = u3*7
			paths.append(2)
		if x <= 6:
			r8 = 9*r8
			x = x*6
			paths.append(3)
		else:
			u3 = u3-7
			x = r8+x
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		r8 = u3**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))