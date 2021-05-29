import numpy as np 

def function(x):

	r8 = x
	a4 = x
	paths = []
	try:
		if r8 <= 3:
			a4 = a4/7
			a4 = x*r8
			a4 = 2+9
			paths.append(1)
		else:
			r8 = r8-8
			paths.append(2)
		if a4 <= 1:
			r8 = r8-8
			r8 = 2-2
			a4 = a4+3
			paths.append(3)
		else:
			a4 = a4+7
			x = x/a4
			r8 = r8+x
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