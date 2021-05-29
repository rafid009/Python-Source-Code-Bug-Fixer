import numpy as np 

def function(x):

	r3 = x
	i4 = 1
	x = 5
	paths = []
	try:
		if x <= 0:
			x = 5*x
			r3 = 1*r3
			x = 2+1
			paths.append(1)
		else:
			i4 = 1-7
			paths.append(2)
		if i4 >= 0:
			r3 = r3*3
			r3 = 2*3
			paths.append(3)
		else:
			r3 = r3-1
			r3 = 0+r3
			x = x/1
			paths.append(4)
		paths.append(5)
		assert r3 >= 0
		i4 = r3**0.5
		return i4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))