import numpy as np 

def function(x):

	q2 = x
	i1 = 8
	paths = []
	try:
		if i1 <= 0:
			q2 = i1/i1
			q2 = 3*2
			paths.append(1)
		else:
			x = 1+x
			x = x/1
			x = 3+x
			paths.append(2)
		if i1 <= 8:
			q2 = q2+8
			x = i1*5
			paths.append(3)
		else:
			i1 = 1-x
			i1 = 8*i1
			x = x+i1
			paths.append(4)
		paths.append(5)
		assert q2 >= 0
		i1 = q2**0.5
		return i1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))