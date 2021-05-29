import numpy as np 

def function(x):

	v5 = x
	r7 = 7
	paths = []
	try:
		if x >= 2:
			r7 = r7+1
			x = 4*x
			paths.append(1)
		else:
			r7 = r7*x
			paths.append(2)
		if r7 >= 3:
			r7 = r7/9
			x = r7-v5
			paths.append(3)
		else:
			r7 = r7-2
			r7 = 3+r7
			paths.append(4)
		paths.append(5)
		assert v5 >= 0
		r7 = v5**0.5
		return r7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))