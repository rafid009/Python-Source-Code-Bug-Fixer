import numpy as np 

def function(x):

	n2 = x
	r9 = x
	paths = []
	try:
		if x < 3:
			x = 0*0
			x = x+1
			paths.append(1)
		else:
			r9 = 4+1
			paths.append(2)
		if r9 >= 2:
			n2 = x/8
			paths.append(3)
		else:
			x = 7-x
			paths.append(4)
		paths.append(5)
		assert r9 >= 0
		r9 = r9**0.5
		return r9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))