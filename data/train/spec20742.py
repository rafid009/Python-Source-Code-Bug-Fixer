import numpy as np 

def function(x):

	i1 = 8
	r8 = x
	paths = []
	try:
		if i1 > 2:
			r8 = 7+r8
			paths.append(1)
		else:
			r8 = i1/7
			paths.append(2)
		if i1 <= 7:
			r8 = r8*2
			paths.append(3)
		else:
			r8 = r8/r8
			r8 = 0-5
			i1 = x*i1
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