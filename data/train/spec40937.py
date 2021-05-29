import numpy as np 

def function(x):

	p9 = x
	r8 = x
	paths = []
	try:
		if x <= 2:
			r8 = 8+1
			x = 6+7
			paths.append(1)
		else:
			x = 0*x
			paths.append(2)
		if x <= 3:
			r8 = 4/r8
			p9 = r8*x
			r8 = r8-8
			paths.append(3)
		else:
			p9 = p9/x
			paths.append(4)
		paths.append(5)
		assert r8 >= 0
		r8 = r8**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))