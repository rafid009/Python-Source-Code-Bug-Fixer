import numpy as np 

def function(x):

	r8 = 1
	v7 = 2
	paths = []
	try:
		if v7 > 9:
			r8 = r8-9
			paths.append(1)
		else:
			v7 = x*v7
			r8 = x*r8
			paths.append(2)
		if x > 1:
			r8 = r8-2
			paths.append(3)
		else:
			v7 = x*5
			x = x*0
			paths.append(4)
		paths.append(5)
		assert v7 >= 0
		r8 = v7**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))