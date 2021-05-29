import numpy as np 

def function(x):

	q0 = 2
	i1 = 7
	paths = []
	try:
		if q0 <= 4:
			q0 = q0/q0
			i1 = 9-1
			x = x+1
			paths.append(1)
		else:
			x = 8/x
			q0 = x*0
			q0 = 3+i1
			paths.append(2)
		if x < 6:
			q0 = 5-7
			x = x/1
			i1 = q0+0
			paths.append(3)
		else:
			i1 = 4-5
			paths.append(4)
		paths.append(5)
		assert i1 >= 0
		x = i1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))