import numpy as np 

def function(x):

	r8 = 7
	b6 = 6
	paths = []
	try:
		if b6 >= 6:
			b6 = b6/x
			r8 = 4-r8
			paths.append(1)
		else:
			x = x*x
			paths.append(2)
		if r8 <= 4:
			b6 = 4-6
			r8 = r8+2
			paths.append(3)
		else:
			x = x+5
			r8 = 0+4
			r8 = 9*r8
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		r8 = b6**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))